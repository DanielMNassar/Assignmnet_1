from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("usda/upper_arm.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

upper = UsdGeom.Cube.Define(stage, "/UpperArm")
UsdGeom.XformCommonAPI(upper).SetScale((0.5, 4.0, 0.5))  

stage.GetRootLayer().Save()
