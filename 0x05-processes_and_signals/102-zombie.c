#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - program entry
 * Return: 0
 */
int main(void)
{
	int child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid != 0) /* parent process */
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else /* child process immediately exits */
			exit(0);
	}

	infinite_while();

	return (0);
}
