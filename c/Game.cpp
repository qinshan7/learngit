#include"stdafx.h"
#include"Game.h"
#include"GameLib.h"
//假设当前坐标：3,2
int main() {
	while (1)
	{
	cleanAll;
	Life = 1;
	Init();
	SetTitle("蛊真人");
	SetColor(4, 7);
	Center("蛊真人", 0);
	Center("魔子出山\n", 1);
	SetColor(10, 0);
	ShowWelcome();
	SetPosition(0, 10);
	ShowInfomation();
	ShowMainMenu();
	SetPosition(0, 5);
	ShowMap();
	while (1)
	{
		key = _getch();
		if (key == -32)
		{
			continue;
		}
		if (key == '1' || key == '2' || key == '3' || key == '4') 
		{
			cleanInfo;
			SetPosition(36, 11);
			ProcessMainMenu(key);
			if (Life == 0)
				break;
			SetPosition(80, 17);
			continue;
		}
		else if (key == 72)//上
		{
			Y--;
		}
		else if (key == 77)//右
		{
			X++;
		}
		else if (key == 80)//下
		{
			Y++;
		}
		else if (key == 75)//左
		{
			X--;
		}
//		else if (key == 53)
//		{
//			cleanAll;
//			Center("You dead", 15);
//			Sleep(2000);
//			break;
//		}
		if (X > 2)X = 0;
		if (X < 0)X = 2;
		if (Y > 2)Y = 0;
		if (Y < 0)Y = 2;
		SetPosition(0, 5);
		ShowMap();
	}
	}

	return 0;
}