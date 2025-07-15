#ifndef BSP_H_
#define BSP_H_

#include "interfaces/serial_interface.h"
#include "stdint.h"
#include <stdbool.h>

/**************************************************************************************************\
* Public macros
\**************************************************************************************************/

#define BSP_TICKS_PER_SEC         1000U
#define MILLISECONDS_TO_TICKS(ms) ((ms) * ((BSP_TICKS_PER_SEC) / 1000))

/**************************************************************************************************\
* Public type definitions
\**************************************************************************************************/

/**************************************************************************************************\
* Public memory declarations
\**************************************************************************************************/

void BSP_Init(void);
void BSP_terminate(int16_t result);

/**************************************************************************************************\
* Public prototypes
\**************************************************************************************************/

/**
 ***************************************************************************************************
 * @brief   Millisecond Tick
 **************************************************************************************************/
uint32_t BSP_Get_Milliseconds_Tick(void);

/**
 ***************************************************************************************************
 * @brief   Functions for blinky LED
 **************************************************************************************************/
void BSP_LED_On(void);
void BSP_LED_Off(void);
void BSP_debug_gpio_on(void);
void BSP_debug_gpio_off(void);
void BSP_debug_gpio_toggle(void);

/**
 ***************************************************************************************************
 * @brief   Retrieve Serial IO interface for the UART Interface serial comms channels
 **************************************************************************************************/
const Serial_IO_T *BSP_Get_Serial_IO_Interface_UART();

/**
 ***************************************************************************************************
 * @brief   Perform a reset of the microcontroller
 **************************************************************************************************/
__attribute__((noreturn)) void BSP_SystemReset(void);

/**
 ***************************************************************************************************
 * @brief   Read the microcontroller's RCC CSR Register.
 **************************************************************************************************/
uint32_t BSP_RCC_CSR_Read(void);

/**
 ***************************************************************************************************
 * @brief   Clear reset flags indicated by the RCC CSR Register.
 **************************************************************************************************/
void BSP_RCC_CSR_ClearResetFlags(void);

/**
 ***************************************************************************************************
 * @brief   Read the microcontroller's assigned backup RAM, a single uint32 value, with index.
 *          Backup RAM is some portion of RAM that survives typical processor reset conditions,
 *          for example, a software driven reset of the microcontroller.
 **************************************************************************************************/
bool BSP_Backup_RAM_Read(int index, uint32_t *output);

/**
 ***************************************************************************************************
 * @brief   Write a value to the microcontroller's assigned backup RAM.
 *          See BSP_Backup_RAM_Read(...) for further background.
 **************************************************************************************************/
void BSP_Backup_RAM_Write(int index, uint32_t value);

#endif // BSP_H_
