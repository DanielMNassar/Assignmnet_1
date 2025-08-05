from pxr import Usd, UsdGeom, Sdf, Gf
import math


stage = Usd.Stage.CreateNew("animated_robot.usda")
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)


root_layer = stage.GetRootLayer()
root_layer.startTimeCode = 1
root_layer.endTimeCode = 192


UsdGeom.Xform.Define(stage, "/RobotRoot")
robot_ref = stage.DefinePrim("/RobotRoot/Robot")
robot_ref.GetReferences().AddReference("robot.usda")


base_path = "/RobotRoot/Robot/Base"
base_prim = stage.GetPrimAtPath(base_path)

if base_prim and base_prim.IsValid():
    base_xform = UsdGeom.Xform(base_prim)
    orient_op = base_xform.AddOrientOp(opSuffix="baseSpin")

    for frame in range(1, 193):
        angle_deg = (frame - 1) * 360.0 / 191.0
        angle_rad = math.radians(angle_deg)
        quat = Gf.Quatf(math.cos(angle_rad / 2), Gf.Vec3f(0, 0, math.sin(angle_rad / 2)))
        orient_op.Set(quat, Usd.TimeCode(frame))
else:
    print(f"[WARNING] Could not find: {base_path}")


upper_arm_path = "/RobotRoot/Robot/UpperArm"
upper_arm_prim = stage.GetPrimAtPath(upper_arm_path)

if upper_arm_prim and upper_arm_prim.IsValid():
    upper_arm_xform = UsdGeom.Xform(upper_arm_prim)
    twist_op = upper_arm_xform.AddRotateYOp(opSuffix="armTwist")

    for frame in range(1, 193):
        if frame <= 96:
            twist_angle = (frame - 1) * 45.0 / 95.0
        else:
            twist_angle = 45.0 - ((frame - 96) * 45.0 / 96.0)
        twist_op.Set(twist_angle, Usd.TimeCode(frame))
else:
    print(f"[WARNING] Could not find: {upper_arm_path}")


gripper_path = "/RobotRoot/Robot/Gripper"
gripper_prim = stage.GetPrimAtPath(gripper_path)

if gripper_prim and gripper_prim.IsValid():
    gripper_xform = UsdGeom.Xform(gripper_prim)
    scale_op = gripper_xform.AddScaleOp(opSuffix="gripperOpen")

    for frame in range(1, 193):
        if frame <= 96:
            scale_factor = 1.0 + (frame - 1) * 1.0 / 95.0
        else:
            scale_factor = 2.0 - ((frame - 96) * 1.0 / 96.0)
        scale_vec = Gf.Vec3f(scale_factor, scale_factor, scale_factor)
        scale_op.Set(scale_vec, Usd.TimeCode(frame))
else:
    print(f"[WARNING] Could not find: {gripper_path}")


stage.GetRootLayer().Save()

