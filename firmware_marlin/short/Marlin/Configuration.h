//#define MANUAL_PROBE_START_Z
#define BLTOUCH
//#define BLTOUCH

#define X_PROBE_OFFSET_FROM_EXTRUDER 49
#define Y_PROBE_OFFSET_FROM_EXTRUDER -18
#define Y_PROBE_OFFSET_FROM_EXTRUDER 10
//===========================================================================
//============================= Z Probe Options =============================
//===========================================================================
 * Enable this option for a probe connected to any pin except Z-Min.
 * (By default Marlin assumes the Z-Max endstop pin.)
 * To use a custom Z Probe pin, set Z_MIN_PROBE_PIN below.
 *
 *  - The simplest option is to use a free endstop connector.
 *  - Use 5V for powered (usually inductive) sensors.

//#define PROBE_MANUALLY
//#define MANUAL_PROBE_START_Z 0.2
#define BLTOUCH

#define X_PROBE_OFFSET_FROM_EXTRUDER 49
#define Y_PROBE_OFFSET_FROM_EXTRUDER -18

#define MULTIPLE_PROBING 2

* Probe Type
 *
 * Allen Key Probes, Servo Probes, Z-Sled Probes, FIX_MOUNTED_PROBE, etc.
 * Activate one of these to use Auto Bed Leveling below.
 */

//#define AUTO_BED_LEVELING_3POINT
//#define AUTO_BED_LEVELING_LINEAR
#define AUTO_BED_LEVELING_BILINEAR
//#define AUTO_BED_LEVELING_UBL
//#define MESH_BED_LEVELING

  //#define GRID_MAX_POINTS_X 3
  #define GRID_MAX_POINTS_X 4

  #define LEFT_PROBE_BED_POSITION 64
  #define RIGHT_PROBE_BED_POSITION 345
  #define FRONT_PROBE_BED_POSITION 15
  #define BACK_PROBE_BED_POSITION 225
  //===========================================================================
  //========================= Unified Bed Leveling ============================
  //===========================================================================
  //#define AUTO_BED_LEVELING_3POINT
#define AUTO_BED_LEVELING_BILINEAR
