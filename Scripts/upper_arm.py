from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("upperarm.usda")
upper_arm = UsdGeom.Xform.Define(stage, "/UpperArm")
UsdGeom.XformCommonAPI(upper_arm).SetTranslate((0, 3, 0))

cube = UsdGeom.Cube.Define(stage, "/UpperArm/Geom")
UsdGeom.XformCommonAPI(cube).SetScale((0.4, 2, 0.4))
UsdGeom.XformCommonAPI(cube).SetTranslate((0, 1, 0))
cube.CreateDisplayColorAttr([(0.7, 0.7, 0.7)])  # Light grey

stage.SetDefaultPrim(upper_arm.GetPrim())
stage.GetRootLayer().Save()
