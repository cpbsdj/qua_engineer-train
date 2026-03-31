import gymnasium as gym

from . import agents

gym.register(
    id="RobotLab-Isaac-Velocity-Flat-Qua_Engineer-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.flat_env_cfg:QUA_ENGINEERFlatEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:QUA_ENGINEERFlatPPORunnerCfg",
        # "cusrl_cfg_entry_point": f"{agents.__name__}.cusrl_ppo_cfg:QUA_ENGINEERFlatTrainerCfg",
    },
)

gym.register(
    id="RobotLab-Isaac-Velocity-Rough-Qua_Engineer-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.rough_env_cfg:QUA_ENGINEERRoughEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:QUA_ENGINEERRoughPPORunnerCfg",
        # "cusrl_cfg_entry_point": f"{agents.__name__}.cusrl_ppo_cfg:QUA_ENGINEERRoughTrainerCfg",
    },
)