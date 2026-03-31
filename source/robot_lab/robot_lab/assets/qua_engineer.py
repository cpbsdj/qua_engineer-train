from robot_lab.assets import ISAACLAB_ASSETS_DATA_DIR

import isaaclab.sim as sim_utils
from isaaclab.actuators import DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg



QUA_ENGINEER_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        fix_base=False,
        merge_fixed_joints=True,
        # merge_fixed_joints=False,
        replace_cylinders_with_capsules=False,
        asset_path=f"{ISAACLAB_ASSETS_DATA_DIR}/Robots/qua_engineer/qua_engineer_description/urdf/qua_engineer.urdf",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        joint_drive=sim_utils.UrdfConverterCfg.JointDriveCfg(
            gains=sim_utils.UrdfConverterCfg.JointDriveCfg.PDGainsCfg(stiffness=0, damping=0)
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.40),
        joint_pos={
            ".*L_hip_joint": 0.0,
            ".*R_hip_joint": -0.0,
            "F.*_thigh_joint": 0.5,
            "R.*_thigh_joint": -0.5,
            "F.*_calf_joint": -0.9,
            "R.*_calf_joint": 0.9,
            # ".*L_hip_joint": 0.0,
            # ".*R_hip_joint": -0.0,
            # "F.*_thigh_joint": 0.5,
            # "R.*_thigh_joint": 0.5,
            # "F.*_calf_joint": -0.9,
            # "R.*_calf_joint": -1.35,
            # ".*_arm_.*":0.0
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.9,
    actuators={
        "calf": DCMotorCfg(
            joint_names_expr=[".*_calf_joint"],
            # effort_limit=270,
            # saturation_effort=270,
            # velocity_limit=26.2,
            # effort_limit=23.5,
            # saturation_effort=23.5,
            # velocity_limit=30,
            effort_limit=90,
            saturation_effort=90,
            velocity_limit=78.5,
            stiffness=25.0,
            damping=0.5,
            # stiffness=50.0,
            # damping=1.0,
            friction=0.0,
        ),
        "thigh": DCMotorCfg(
            joint_names_expr=[".*_thigh_joint"],
            effort_limit=90,
            saturation_effort=90,
            velocity_limit=78.5,
            # effort_limit=23.5,
            # saturation_effort=23.5,
            # velocity_limit=30,
            stiffness=25.0,
            damping=0.5,
            # stiffness=50.0,
            # damping=1.0,
            friction=0.0,
        ),
        "hip": DCMotorCfg(
            joint_names_expr=[".*_hip_joint"],
            effort_limit=75,
            saturation_effort=75,
            velocity_limit=58.5,
            # effort_limit=23.5,
            # saturation_effort=23.5,
            # velocity_limit=30,
            stiffness=25.0,
            damping=0.5,
            # stiffness=50.0,
            # damping=1.0,    
            friction=0.0,
        ),
        # "arms": DCMotorCfg(
        #     joint_names_expr=[".*_arm_.*"],
        #     effort_limit=75,
        #     saturation_effort=75,
        #     velocity_limit=58.5,
        #     stiffness=25.0,
        #     damping=0.5,
        #     friction=0.0,
        # ),
    },
)