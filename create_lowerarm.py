from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("usda/lower_arm.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

lower = UsdGeom.Cube.Define(stage, "/LowerArm")
UsdGeom.XformCommonAPI(lower).SetScale((0.5, 4.0, 0.5))  

stage.GetRootLayer().Save()
