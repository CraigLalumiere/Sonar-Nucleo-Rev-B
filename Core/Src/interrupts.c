#include "bsp.h"
#include "pubsub_signals.h"
#include "stm32g4xx_hal.h"

// extern TIM_HandleTypeDef htim2;
extern ADC_HandleTypeDef hadc2;

inline void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef *hadc)
{
    if (hadc->Instance == hadc2.Instance)
    {
        static QEvt const event = QEVT_INITIALIZER(PUBSUB_ADC2_COMPLETE_SIG);
        QACTIVE_PUBLISH(&event, NULL);
    }
}

// inline void HAL_TIM_PWM_PulseFinishedCallback(TIM_HandleTypeDef *htim)
// {
//     static int i = 0;
//     if (htim->Instance == htim2.Instance)
//     {
//         i++;
//         static QEvt const event = QEVT_INITIALIZER(PUBSUB_RECEIVE_COMPLETE_SIG);
//         QACTIVE_PUBLISH(&event, NULL);
//     }
// }