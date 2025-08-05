from pxr import Usd, UsdGeom, UsdPhysics, UsdShade, Gf

stage = Usd.Stage.CreateNew("physics_robot.usda")
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(192)

UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

physics_scene = UsdPhysics.Scene.Define(stage, "/World/PhysicsScene")
physics_scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, -1.0, 0.0))
physics_scene.CreateGravityMagnitudeAttr().Set(9.81)

root_xform = UsdGeom.Xform.Define(stage, "/World")

robot_xform = UsdGeom.Xform.Define(stage, "/World/PhysicsRobot")
robot_prim = stage.DefinePrim("/World/PhysicsRobot/Robot")
robot_prim.GetReferences().AddReference("./animated_robot.usda", "/RobotRoot")
robot_xform.AddTranslateOp().Set(Gf.Vec3f(0.0, 5.0, 0.0))

UsdPhysics.RigidBodyAPI.Apply(robot_prim)
UsdPhysics.CollisionAPI.Apply(robot_prim)

robot_material_prim = UsdGeom.Xform.Define(stage, "/World/RobotMaterial").GetPrim()
robot_material = UsdPhysics.MaterialAPI.Apply(robot_material_prim)
robot_material.CreateStaticFrictionAttr().Set(1.0)
robot_material.CreateDynamicFrictionAttr().Set(0.7)
robot_material.CreateRestitutionAttr().Set(0.9)

UsdShade.MaterialBindingAPI.Apply(robot_prim).Bind(UsdShade.Material(robot_material_prim))

ground = UsdGeom.Cube.Define(stage, "/World/GroundCube")
ground.CreateSizeAttr().Set(1.0)

ground_xform = UsdGeom.Xformable(ground)
ground_xform.AddScaleOp().Set(Gf.Vec3f(20.0, 0.1, 20.0))
ground_xform.AddTranslateOp().Set(Gf.Vec3f(0.0, -0.05, 0.0))

UsdPhysics.CollisionAPI.Apply(ground.GetPrim())
UsdPhysics.RigidBodyAPI.Apply(ground.GetPrim()).CreateKinematicEnabledAttr().Set(True)

ground_material_prim = UsdGeom.Xform.Define(stage, "/World/GroundMaterial").GetPrim()
ground_material = UsdPhysics.MaterialAPI.Apply(ground_material_prim)
ground_material.CreateStaticFrictionAttr().Set(0.8)
ground_material.CreateDynamicFrictionAttr().Set(0.6)
ground_material.CreateRestitutionAttr().Set(0.1)

UsdShade.MaterialBindingAPI.Apply(ground.GetPrim()).Bind(UsdShade.Material(ground_material_prim))

stage.GetRootLayer().Save()
print("✅ Created physics_robot.usda with animated robot and physics setup.")
