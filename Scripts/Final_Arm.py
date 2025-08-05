from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("robot.usda")

robot = UsdGeom.Xform.Define(stage, "/Robot")

base = UsdGeom.Xform.Define(stage, "/Robot/Base")
UsdGeom.XformCommonAPI(base).SetRotate((90, 0, 0), UsdGeom.XformCommonAPI.RotationOrderXYZ)
base.GetPrim().GetReferences().AddReference("base.usda", "/Base")

lower_arm = UsdGeom.Xform.Define(stage, "/Robot/LowerArm")
UsdGeom.XformCommonAPI(lower_arm).SetTranslate((0, 2.0, 0))
lower_arm.GetPrim().GetReferences().AddReference("lowerarm.usda", "/LowerArm")

upper_arm = UsdGeom.Xform.Define(stage, "/Robot/UpperArm")
UsdGeom.XformCommonAPI(upper_arm).SetTranslate((0.2, 4.2, 0))
UsdGeom.XformCommonAPI(upper_arm).SetRotate((0, 0, -30), UsdGeom.XformCommonAPI.RotationOrderXYZ)
upper_arm.GetPrim().GetReferences().AddReference("upperarm.usda", "/UpperArm")

gripper = UsdGeom.Xform.Define(stage, "/Robot/Gripper")
UsdGeom.XformCommonAPI(gripper).SetTranslate((1.55, 6.5, 0))  
gripper.GetPrim().GetReferences().AddReference("gripper.usda", "/Gripper")

stage.SetDefaultPrim(robot.GetPrim())
stage.GetRootLayer().Save()
