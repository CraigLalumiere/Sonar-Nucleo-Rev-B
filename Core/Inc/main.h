/* USER CODE BEGIN Header */
/**
 ******************************************************************************
 * @file           : main.h
 * @brief          : Header for main.c file.
 *                   This file contains the common defines of the application.
 ******************************************************************************
 * @attention
 *
 * Copyright (c) 2024 STMicroelectronics.
 * All rights reserved.
 *
 * This software is licensed under terms that can be found in the LICENSE file
 * in the root directory of this software component.
 * If no LICENSE file comes with this software, it is provided AS-IS.
 *
 ******************************************************************************
 */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32g4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define GAIN_SEL_0_Pin GPIO_PIN_0
#define GAIN_SEL_0_GPIO_Port GPIOC
#define GAIN_SEL_1_Pin GPIO_PIN_1
#define GAIN_SEL_1_GPIO_Port GPIOC
#define GAIN_SEL_2_Pin GPIO_PIN_2
#define GAIN_SEL_2_GPIO_Port GPIOC
#define XDCR_RX_Pin GPIO_PIN_0
#define XDCR_RX_GPIO_Port GPIOA
#define FW_LED_Pin GPIO_PIN_5
#define FW_LED_GPIO_Port GPIOA
#define HV_SENSE_Pin GPIO_PIN_6
#define HV_SENSE_GPIO_Port GPIOA
#define WaterTemp_Pin GPIO_PIN_5
#define WaterTemp_GPIO_Port GPIOC
#define BOOST_EN_Pin GPIO_PIN_0
#define BOOST_EN_GPIO_Port GPIOB
#define XDCR_VREF_Pin GPIO_PIN_1
#define XDCR_VREF_GPIO_Port GPIOB
#define CS_Pin GPIO_PIN_10
#define CS_GPIO_Port GPIOA
#define nHV_DISCHARGE_Pin GPIO_PIN_11
#define nHV_DISCHARGE_GPIO_Port GPIOA
#define DEBUG_GPIO_Pin GPIO_PIN_6
#define DEBUG_GPIO_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
