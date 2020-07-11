#pragma once
#pragma warning(disable : 4996)

#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>

#include<iostream>

#define BUFSIZE (255)

bool checkfilename(char* name) {
	FILE* fp;
	char filename[12 + 1] = "namelist.txt";
	char namelist[BUFSIZE][BUFSIZE];
	bool checkname = false;
	int namelen = 0;

	if ((fp = fopen(filename, "r")) == NULL) {
		;
	}
	else {
		char s[BUFSIZE] = "";
		int k = 0;
		while (fgets(s, BUFSIZE, fp) != NULL) {
			s[strlen(s) - 1] = '\0';
			if (strcmp(name, s) == 0) { checkname = true; }
			strcpy(namelist[k], s);
			k++;
		}
		namelen = k;
		fclose(fp);
	}

	if (!checkname) {
		strcpy(namelist[namelen], name); namelen++;
		if ((fp = fopen(filename, "w")) == NULL) {
			;
		}
		else {
			int k = 0;
			while (k < namelen) {
				fprintf(fp, "%s\n", namelist[k]);
				k++;
			}
		}
		fclose(fp);
	}
	return checkname;
}

void resetfile(char* name, int thismonth, int quizlen)
{
	FILE* fp;
	char filename[BUFSIZE];
	sprintf(filename, "%s.txt", name);

	if ((fp = fopen(filename, "w")) != NULL) {
		bool flag = false;
		int k = 0;
		while (k < quizlen) {
			if (!flag) {
				fprintf(fp, "%d\n", thismonth);
				flag = true;
			}
			else {
				fprintf(fp, "%d %d %d\n", k, 0, 0);
				k++;
			}
		}
	}
	fclose(fp);
}

void writeAnswer(char name[], int nowmonth, int ans, int quiznum) {
	FILE* fp1, * fp2;
	char filename[BUFSIZE];
	int a[BUFSIZE], b[BUFSIZE], c[BUFSIZE];
	int n;

	sprintf(filename, "%s.txt", name);

	if ((fp1 = fopen(filename, "r")) == NULL) {
		return;
	}
	else {
		char s[255] = "", * ptr[3];
		int k = 0;
		fgets(s, BUFSIZE, fp1); s[strlen(s) - 1] = '\0'; //Delete thismonth data (not use)

		while (fgets(s, BUFSIZE, fp1) != NULL) {
			s[strlen(s) - 1] = '\0';
			ptr[0] = strtok(s, " "); ptr[1] = strtok(NULL, " "); ptr[2] = strtok(NULL, " ");
			a[k] = atoi(ptr[0]); b[k] = atoi(ptr[1]); c[k] = atoi(ptr[2]);

			k++;
		}
		n = k;

	}
	fclose(fp1);

	b[quiznum] = 1;
	c[quiznum] = ans;

	if ((fp2 = fopen(filename, "w")) == NULL) {
		return;
	}
	else {
		bool flag = false;
		int k = 0;
		while (k < n) {
			if (!flag) {
				fprintf(fp2, "%d\n", nowmonth);
				flag = true;
			}
			else {
				fprintf(fp2, "%d %d %d\n", a[k], b[k], c[k]);
				k++;
			}
		}
	}
	fclose(fp2);
}

void txt2csv(char* name, int lastlogmonth) {
	char fname1[BUFSIZE], fname2[BUFSIZE];
	sprintf(fname1, "%s.txt", name);
	sprintf(fname2, "%s_%d.csv", name, lastlogmonth);

	FILE* fp1;
	FILE* fp2 = fopen(fname2, "w");
	FILE* fp3 = fopen("quiz.txt", "r");
	int num = 0, ans = 0;
	char s[BUFSIZE] = "", t[BUFSIZE] = "";
	int res = 0;
	char* ptr[2];
	char* ptr2[3];
	if ((fp1 = fopen(fname1, "r")) == NULL) {
		return;
	}
	else {
		fprintf(fp2, "Question, o or x, Correct Ans, Ans\n");
		int k = 0;
		fgets(t, BUFSIZE, fp1); t[strlen(t) - 1] = '\0';
		while (true) {
			fgets(s, BUFSIZE, fp3); s[strlen(s) - 1] = '\0';
			ptr[0] = strtok(s, " "); ptr[1] = strtok(NULL, " ");
			num = atoi(ptr[0]); ans = atoi(ptr[1]);
			if (num == -1 && ans == -1) { break; }
			fgets(s, BUFSIZE, fp3); s[strlen(s) - 1] = '\0';


			fgets(t, BUFSIZE, fp1); t[strlen(t) - 1] = '\0';
			ptr2[0] = strtok(t, " "); ptr2[1] = strtok(NULL, " "); ptr2[2] = strtok(NULL, " ");
			res = atoi(ptr2[2]);

			if (ans == res) {
				fprintf(fp2, "%s, O, %d, %d\n", s, ans, res);
			}
			else if (res == 0) {
				fprintf(fp2, "%s, ¢, %d, %d\n", s, ans, res);;
			}
			else {
				fprintf(fp2, "%s, X, %d, %d\n", s, ans, res);
			}
		}
	}
	fclose(fp1);
	fclose(fp2);
	fclose(fp3);
}


int getQuizNumber(char* name, int len, int* lastlogmonth)
{
	srand((unsigned int)time(NULL));

	int Quiznumber[BUFSIZE] = {};
	int quiznumber = 0;

	FILE* fp;
	char fname[BUFSIZE];
	sprintf(fname, "%s.txt", name);

	if ((fp = fopen(fname, "r")) == NULL) {
		quiznumber = rand() % (len);
	}
	else {
		int Listlen = 0, k = 0;
		char s[BUFSIZE] = "", * ptr[3];
		fgets(s, BUFSIZE, fp); s[strlen(s) - 1] = '\0';
		*lastlogmonth = atoi(s);
		//cout << *lastlogmonth << endl;

		int a[BUFSIZE], b[BUFSIZE];
		while (fgets(s, BUFSIZE, fp) != NULL) {
			s[strlen(s) - 1] = '\0';
			ptr[0] = strtok(s, " "); ptr[1] = strtok(NULL, " ");
			a[k] = atoi(ptr[0]); b[k] = atoi(ptr[1]);
			if (b[k] == 0) {
				Quiznumber[Listlen] = a[k];
				Listlen++;
			}
			k++;
		}
		fclose(fp);

		int idx = (Listlen == 0) ? -1 : rand() % Listlen;
		quiznumber = (idx == -1) ? -1 : Quiznumber[idx];
	}
	return quiznumber;
}

int getQuizArray(char QuizArray[][BUFSIZE], int CorrectAnsArray[]) {
	int quizlen = 0;
	FILE* fp;

	if ((fp = fopen("quiz.txt", "r")) == NULL) {
		return -1;
	}
	else {
		char s[BUFSIZE] = "";
		int num = 0, ans = 0;
		char* ptr[2];
		while (true) {
			fgets(s, BUFSIZE, fp); s[strlen(s) - 1] = '\0';
			ptr[0] = strtok(s, " "); ptr[1] = strtok(NULL, " ");
			num = atoi(ptr[0]); ans = atoi(ptr[1]);
			if (num == -1 && ans == -1) { break; }
			fgets(s, BUFSIZE, fp); s[strlen(s) - 1] = '\0';
			strcpy(QuizArray[quizlen], s);
			CorrectAnsArray[quizlen] = ans;
			quizlen++;
		}
		fclose(fp);
	}
	return quizlen;
}

int getMonth() {
	time_t t = time(&t);
	struct tm* tm = localtime(&t);
	//printf("%2d\n", tm->tm_mon);
	return (int)(tm->tm_mon + 1);
}
