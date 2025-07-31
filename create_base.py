from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("usda/base.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

base = UsdGeom.Cylinder.Define(stage, "/Base")
base.CreateRadiusAttr(2.0)
base.CreateHeightAttr(0.5)

stage.GetRootLayer().Save()
