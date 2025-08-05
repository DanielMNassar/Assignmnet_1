from pxr import Usd, UsdGeom, Sdf, Gf

stage = Usd.Stage.CreateNew("multiple_animations.usda")
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)

rootLayer = stage.GetRootLayer()
rootLayer.startTimeCode = 1
rootLayer.endTimeCode = 192

UsdGeom.Xform.Define(stage, "/MultipleRobots")

# Original Robot
original_xform = UsdGeom.Xform.Define(stage, "/MultipleRobots/Original")
original_prim = stage.DefinePrim("/MultipleRobots/Original/RobotRoot")
original_prim.GetReferences().AddReference("./animated_robot.usda", "/RobotRoot")
original_xform.AddTranslateOp().Set(Gf.Vec3f(-10.0, 0.0, 0.0))

# Shifted Robot (offset = 48)
shifted_xform = UsdGeom.Xform.Define(stage, "/MultipleRobots/Shifted")
shifted_prim = stage.DefinePrim("/MultipleRobots/Shifted/RobotRoot")
shifted_ref = Sdf.Reference("./animated_robot.usda", "/RobotRoot", Sdf.LayerOffset(offset=48.0))
shifted_prim.GetReferences().AddReference(shifted_ref)
shifted_xform.AddTranslateOp().Set(Gf.Vec3f(0.0, 0.0, 0.0))

# Half Speed Robot (scale = 0.5)
half_speed_xform = UsdGeom.Xform.Define(stage, "/MultipleRobots/HalfSpeed")
half_speed_prim = stage.DefinePrim("/MultipleRobots/HalfSpeed/RobotRoot")
half_speed_ref = Sdf.Reference("./animated_robot.usda", "/RobotRoot", Sdf.LayerOffset(scale=0.5))
half_speed_prim.GetReferences().AddReference(half_speed_ref)
half_speed_xform.AddTranslateOp().Set(Gf.Vec3f(10.0, 0.0, 0.0))

stage.GetRootLayer().Save()
