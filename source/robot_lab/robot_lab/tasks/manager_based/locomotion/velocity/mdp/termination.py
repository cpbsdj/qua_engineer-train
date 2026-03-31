from __future__ import annotations

import torch
from typing import TYPE_CHECKING, Literal

import isaaclab.utils.math as math_utils
from isaaclab.assets import Articulation, RigidObject
from isaaclab.managers import  ManagerTermBase, EventTermCfg, SceneEntityCfg
from isaaclab.utils.math import sample_uniform

from .utils import is_env_assigned_to_terrain

if TYPE_CHECKING:
    from isaaclab.envs import ManagerBasedEnv, ManagerBasedRLEnv




def base_tilt_termination(
    env: ManagerBasedRLEnv,
    max_tilt_angle: float = 60.0,
    asset_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
) -> torch.Tensor:
    """Terminate when the base tilt angle exceeds the threshold.
    
    Args:
        env: The environment.
        max_tilt_angle: Maximum allowed tilt angle in degrees. Default is 60 degrees.
        asset_cfg: The asset configuration.
        
    Returns:
        A boolean tensor indicating which environments should terminate.
    """
    # extract the asset
    asset: RigidObject = env.scene[asset_cfg.name]
    
    # get the projected gravity vector in base frame (normalized)
    # projected_gravity_b shape: (num_envs, 3), typically [gx, gy, gz]
    proj_grav = asset.data.projected_gravity_b
    
    # compute the tilt angle cosine (absolute value of z-component)
    # when base is upright: |gz| ≈ 1.0 (angle = 0°)
    # when base is tilted 60°: |gz| = cos(60°) = 0.5
    cos_tilt = torch.abs(proj_grav[:, 2])
    
    # convert max_tilt_angle to cosine threshold
    cos_threshold = torch.cos(torch.tensor(max_tilt_angle * torch.pi / 180.0, device=env.device))
    
    # terminate if tilt angle exceeds threshold (cos_tilt < cos_threshold)
    return cos_tilt < cos_threshold