from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("usda/gripper.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

gripper = UsdGeom.Sphere.Define(stage, "/Gripper")
gripper.CreateRadiusAttr(0.2)

stage.GetRootLayer().Save()
