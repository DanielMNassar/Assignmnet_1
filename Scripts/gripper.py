from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("gripper.usda")
gripper = UsdGeom.Xform.Define(stage, "/Gripper")
UsdGeom.XformCommonAPI(gripper).SetTranslate((0, 5, 0))

sphere = UsdGeom.Sphere.Define(stage, "/Gripper/Geom")
UsdGeom.XformCommonAPI(sphere).SetScale((0.4, 0.4, 0.4))
UsdGeom.XformCommonAPI(sphere).SetTranslate((0, 0.4, 0))
sphere.CreateDisplayColorAttr([(0.2, 1.0, 0.2)])  # Green

stage.SetDefaultPrim(gripper.GetPrim())
stage.GetRootLayer().Save()
