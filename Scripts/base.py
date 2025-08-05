from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("base.usda")
base = UsdGeom.Xform.Define(stage, "/Base")
UsdGeom.XformCommonAPI(base).SetTranslate((0, 0, 0))

cylinder = UsdGeom.Cylinder.Define(stage, "/Base/Geom")
UsdGeom.XformCommonAPI(cylinder).SetScale((1.5, 0.5, 1.5))
UsdGeom.XformCommonAPI(cylinder).SetTranslate((0, 0.5, 0))
cylinder.CreateDisplayColorAttr([(0.2, 0.2, 0.2)])  # Dark grey

stage.SetDefaultPrim(base.GetPrim())
stage.GetRootLayer().Save()
