#include <string.h>
#include <stdio.h>

char ch_new[1003];

int check1(char x)
{
	int p = 0;
	if (x == '*' || x == '/')
		p = 3;
	else if (x == '+' || x == '-')
		p = 2;
	else if (x== ')')
		p = 1;
	else if (x== '(')
		p = 4;
	return p;
}
int check2(char x)
{
	int p = 0;
	if (x == '*' || x == '/')
		p = 3;
	else if (x == '+' || x == '-')
		p = 2;
	else if (x== ')')
		p = 4;
	else if (x== '(')
		p = 1;
	return p;
}
void ChangeToBehind(char ch[])
{
	int len = strlen(ch), num = 0, l = 0, i, j, top = 0;
	char heap[2000];
	ch_new[0] = 0;
	heap[0] = '#';
	ch[len] = '#';
	for (i = 0; i <= len; i++)
	{
		if (ch[i] >= '0' && ch[i] <= '9')
			num++;
		else
		{
			for (j = 0; j < num; j++)
				ch_new[l + j] = ch[i - num + j];
			ch_new[l + num] = ' ';
			l = l + num + 1;
			num = 0;
			while (check1(ch[i]) <= check2(heap[top]))
			{
				if (top == 0)
					break;
				if (heap[top] != '('){
					ch_new[l] = heap[top];
					l = l + 1;
				}
				else if (ch[i] == ')'){
					top--;
					break;
				}
				top --;
			}
			heap[++top] = ch[i];
		}
	}
}

float getResult(char ch[])
{
	int len = strlen(ch);
	int top = 0, num = 0, i, flag = 0;
	float sta[1003];
	for (i = 0; i < len; i++)
	{
		if (ch[i] >= '0' && ch[i] <= '9')
		{
			flag = 1;
			num = num * 10 + ch[i] - '0';
		}
		else
		{
			if (flag == 1){
				sta[top] = num;
				top = top + 1;
			}
			num = 0;
			flag = 0;
			if (ch[i] == '+'){
				top = top - 1;
				sta[top - 1] = sta[top - 1] + sta[top];
			}
			else if (ch[i] == '-'){
				top = top - 1;
				sta[top - 1] = sta[top - 1] - sta[top];
			}
			else if (ch[i] == '*'){
				top = top - 1;
				sta[top - 1] = sta[top - 1] * sta[top];
			}
			else if (ch[i] == '/'){
				top = top - 1;
				sta[top - 1] = sta[top - 1] / sta[top];
			}
		}
	}
	return sta[0];
}
void test(char ch[])
{
	ChangeToBehind(ch);
	printf("%lf\n",getResult(ch_new));
}
int main()
{
	char ch[] = "1+(5-2)*4/(2+1)";
	test(ch);
	return 0;

}

