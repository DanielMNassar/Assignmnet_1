from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("lowerarm.usda")
lower_arm = UsdGeom.Xform.Define(stage, "/LowerArm")
UsdGeom.XformCommonAPI(lower_arm).SetTranslate((0, 1, 0))

cube = UsdGeom.Cube.Define(stage, "/LowerArm/Geom")
UsdGeom.XformCommonAPI(cube).SetScale((0.4, 2, 0.4))
UsdGeom.XformCommonAPI(cube).SetTranslate((0, 1, 0))
cube.CreateDisplayColorAttr([(0.7, 0.7, 0.7)])  # Light grey

stage.SetDefaultPrim(lower_arm.GetPrim())
stage.GetRootLayer().Save()
