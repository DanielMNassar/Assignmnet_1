from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("robot.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

root = UsdGeom.Xform.Define(stage, "/Robot")

# Base
base = UsdGeom.Xform.Define(stage, "/Robot/Base")
base.GetPrim().GetReferences().AddReference("usda/base.usda")
UsdGeom.XformCommonAPI(base).SetTranslate((0, 0.25, 0))

# Lower Arm
lower = UsdGeom.Xform.Define(stage, "/Robot/LowerArm")
lower.GetPrim().GetReferences().AddReference("usda/lower_arm.usda")
UsdGeom.XformCommonAPI(lower).SetTranslate((0, 2.5, 0))

# Upper Arm
upper = UsdGeom.Xform.Define(stage, "/Robot/UpperArm")
upper.GetPrim().GetReferences().AddReference("usda/upper_arm.usda")
UsdGeom.XformCommonAPI(upper).SetTranslate((0, 6.5, 0))

# Gripper
gripper = UsdGeom.Xform.Define(stage, "/Robot/Gripper")
gripper.GetPrim().GetReferences().AddReference("usda/gripper.usda")
UsdGeom.XformCommonAPI(gripper).SetTranslate((0, 9.5, 0))

stage.GetRootLayer().Save()
