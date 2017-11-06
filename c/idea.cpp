/** @file idea.cpp
 *  @brief Protocol for the IDEA Drive ACM4826
 *  @author Lee Hicks
 *  @copyright MowBotix Inc
 *
 *  This specifically handle the protocol used by Haydonkerk Idea Drive
 *  dated 4-2013
 *
 */

#include <stdio.h>
#include <stdbool.h>

#include "idea.h"

void abort(char * buf, char const * motor_id){
    sprintf(buf, "#%sA\r", motor_id);
}


void enable_encoder(char * buf, char const * motor_id, int deadband, int encoder_res, int motor_res){
    sprintf(buf, "#%sz%d,0,0,10,%d,%d\r", motor_id, deadband, encoder_res, motor_res);
}


void move(char * buf, char const * motor_id, int steps, int speed, int run_cur, int hold_cur, int mode, bool boost){

    steps = steps * 64;

    if(boost == true){
        run_cur += 600;
    }

    sprintf(buf, "#%sM%d,%d,0,0,0,0,%d,%d,%d,%d,50,%d\r", motor_id,
           steps, speed, run_cur, hold_cur, run_cur, run_cur, mode);
}


void set_position(char * buf, char const * motor_id, int position){
    sprintf(buf, "#%sZ%d\r", motor_id, position);
}
