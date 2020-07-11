#pragma once
#pragma warning(disable : 4996)

#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>

#include<iostream>
using namespace std;

#include"function.h"

#define BUFSIZE 255

int main(void)
{
	char QuizArray[BUFSIZE][BUFSIZE];
	char name[BUFSIZE] = "";
	int CorrectAnsArray[BUFSIZE];
	int quizlen = 0;
	int quiznum = 0;

	if ((quizlen = getQuizArray(QuizArray, CorrectAnsArray)) == -1) { return 0; }
	
	while(true) {
		cout << "What's your name: ";
		char name[BUFSIZE] = "mattya"; cin >> name;

		int thismonth = getMonth();
		int lastlogmonth = 0;
		if ((quiznum = getQuizNumber(name, quizlen, &lastlogmonth)) == -1) {
			txt2csv(name, lastlogmonth);
			resetfile(name, thismonth, quizlen);
			cout << "You have already answered all quiestiuons !" << endl;
			continue;
		}

		if (thismonth != lastlogmonth && lastlogmonth != 0) {
			txt2csv(name, lastlogmonth);
			resetfile(name, thismonth, quizlen);
		}

		cout << "Question: " << QuizArray[quiznum] << ": ";
		int ans = 0;  cin >> ans;
		if (ans == CorrectAnsArray[quiznum]) { cout << "True" << endl; }
		else { cout << "False" << endl; }

		if (!checkfilename(name)) {
			resetfile(name, thismonth, quizlen);
		}
		
		writeAnswer(name, thismonth, ans, quiznum);
	
	}
	return 0;
}

