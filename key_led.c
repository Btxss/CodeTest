
#include "s3c2440_soc.h"

void delay(volatile int d)
{
	while (d--);
}

int main(void)
{
	int val1, val2;
	
	/* 设置GPFCON让GPF4/5/6配置为输出引脚 */
	GPFCON &= ~((3<<8) | (3<<10) | (3<<12));
	GPFCON |=  ((1<<8) | (1<<10) | (1<<12));
	/* 配置3个按键引脚为输入引脚:
	 * GPF0(S2),GPF2(S3),GPG3(S4)
	 */
	 GPFCON &= ~((3<<0) | (3<<4)); /* gpf0,2 */
	 GPFCON &= ~ ((3<<6)); /* gpg3 */
	 
	 /* 循环点亮 */
	 while (1)
     
     
     
     
}
