from pydcs_extensions.a4ec.a4ec import A_4E_C
from pydcs_extensions.highdigitsams import highdigitsams
from pydcs_extensions.mb339.mb339 import MB_339PAN
from pydcs_extensions.rafale.rafale import Rafale_M, Rafale_A_S
from pydcs_extensions.su57.su57 import Su_57
import pydcs_extensions.frenchpack.frenchpack as frenchpack

MODDED_AIRPLANES = [A_4E_C, MB_339PAN, Rafale_A_S, Rafale_M, Su_57]
MODDED_VEHICLES = [
    frenchpack._FIELD_HIDE,
    frenchpack._FIELD_HIDE_SMALL,
    frenchpack.SMOKE_SAM_IR,
    frenchpack.SmokeD1,
    frenchpack.SmokeD3,
    frenchpack.AMX_10RCR,
    frenchpack.AMX_10RCR_SEPAR,
    frenchpack.ERC_90,
    frenchpack.MO_120_RT,
    frenchpack._53T2,
    frenchpack.TRM_2000,
    frenchpack.TRM_2000_Fuel,
    frenchpack.TRM_2000_53T2,
    frenchpack.TRM_2000_PAMELA,
    frenchpack.VAB_MEDICAL,
    frenchpack.VAB,
    frenchpack.VAB__50,
    frenchpack.VAB_T20_13,
    frenchpack.VAB_MEPHISTO,
    frenchpack.VAB_MORTIER,
    frenchpack.VBL__50,
    frenchpack.VBL_AANF1,
    frenchpack.VBL,
    frenchpack.VBAE_CRAB,
    frenchpack.VBAE_CRAB_MMP,
    frenchpack.AMX_30B2,
    frenchpack.Tracma_TD_1500,
    frenchpack.Infantry_Soldier_JTAC,
    frenchpack.Char_M551_Sheridan,
    frenchpack.Leclerc_Serie_XXI,
    frenchpack.DIM__TOYOTA_BLUE,
    frenchpack.DIM__TOYOTA_GREEN,
    frenchpack.DIM__TOYOTA_DESERT,
    frenchpack.DIM__KAMIKAZE,
    highdigitsams.SAM_SA_20_S_300PMU1_TR_30N6E,
    highdigitsams.SAM_SA_20_S_300PMU1_TR_30N6E_truck,
    highdigitsams.SAM_SA_20_S_300PMU1_SR_5N66E,
    highdigitsams.SAM_SA_20_S_300PMU1_SR_64N6E,
    highdigitsams.SAM_SA_23_S_300VM_9S15M2_SR,
    highdigitsams.SAM_SA_23_S_300VM_9S19M2_SR,
    highdigitsams.SAM_SA_23_S_300VM_9S32ME_TR,
    highdigitsams.SAM_SA_20_S_300PMU1_LN_5P85CE,
    highdigitsams.SAM_SA_20_S_300PMU1_LN_5P85DE,
    highdigitsams.SAM_SA_10__5V55RUD__S_300PS_LN_5P85CE,
    highdigitsams.SAM_SA_10__5V55RUD__S_300PS_LN_5P85DE,
    highdigitsams.SAM_SA_23_S_300VM_9A83ME_LN,
    highdigitsams.SAM_SA_23_S_300VM_9A82ME_LN,
    highdigitsams.SAM_SA_17_Buk_M1_2_LN_9A310M1_2,
    highdigitsams.SAM_SA_2__V759__LN_SM_90,
    highdigitsams.SAM_HQ_2_LN_SM_90,
    highdigitsams.SAM_SA_3__V_601P__LN_5P73,
    highdigitsams.SAM_SA_20_S_300PMU1_CP_54K6,
    highdigitsams.SAM_SA_23_S_300VM_9S457ME_CP,
    highdigitsams.SAM_SA_24_Igla_S_manpad,
    highdigitsams.SAM_SA_14_Strela_3_manpad
]