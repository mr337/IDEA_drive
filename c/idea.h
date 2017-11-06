/** @file idea.h
 *  @brief Header file for idea.c
 *  @author Lee Hicks
 *  @copyright MowBotix Inc
 *
 *
 */

void abort(char * buf, char const * motor_id);

/** @brief Abort current operation
 *
 *  @param buf Buffer formatted command string will be stored
 *  @param motor_id Motor ID address to send command to
 *  @return Void
 *
 */


void enable_encoder(char * buf, char const * motor_id, int deadband, int encoder_res, int motor_res);

/** @brief Formatted move command ready to be sent to controller
 *
 *  @param buf Buffer formatted command string will be stored
 *  @param motor_id Motor ID address to send command to
 *  @param deadband The 1/64 steps to be in the deadband
 *  @param encoder_res Encoder counter per revolution
 *  @param motor_res Motor steps per single revolution
 *  @return Void
 *
 */


void move(char * buf, char const * motor_id, int steps, int speed, int run_cur, int hold_cur, int mode, bool boost);

/** @brief Formatted move command ready to be sent to controller
 *
 *  @param buf Buffer formatted command string will be stored
 *  @param motor_id Motor ID address to send command to
 *  @param steps The number of steps of whole steps to move (multiplied by 64)
 *  @param speed Number of whole steps per second
 *  @param run_cur Current in milliamps to run - accel and decel with same current
 *  @param run_cur Current in milliamps to hold
 *  @param mode Step mode, 1 to 16 for 16th step
 *  @return Void
 *
 */

void set_position(char * buf, char const * motor_id, int position);

/** @brief Sets encoder position
 *
 *  Useful for resetting the position to 0 or an absolute location
 *
 *  @param buf Buffer formatted command string will be stored
 *  @param motor_id Motor ID address to send command to
 *  @param position Position to set encoder to
 *  @return Void
 *
 */
