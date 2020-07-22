#pragma once
#pragma warning(disable : 4996)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <string>

#include <mysql_driver.h>
#include <mysql_connection.h>
#include <mysql_error.h>
#include <cppconn/Statement.h>
#include <cppconn/ResultSet.h>
#include <cppconn/prepared_statement.h>

#include "strconv.h"

using namespace std;
using namespace sql;

#define BUFFERSIZE (255)

void CheckTotalTable(Statement* stmt)
{

    ResultSet* res = stmt->executeQuery("SELECT Pokemon.num, \
                                                Pokemon.name, \
                                                Color.color, \
                                                Pokemon.height,\
                                                Pokemon.weight, \
                                                Type1.type1, \
                                                Type2.type2 \
                                          FROM Pokemon \
                                          JOIN Color ON Pokemon.color_num = Color.color_num \
                                          JOIN Type1 ON Pokemon.type_num1 = Type1.type_num1 \
                                          JOIN Type2 ON Pokemon.type_num2 = Type2.type_num2 \
                                          ORDER BY Pokemon.num");

    while (res->next())
    {
        cout << "No. " << res->getInt("num") << ", ";
        
        string utf8_str = res->getString("name");
        string sjis_str = utf8_to_sjis(utf8_str);
        cout << "name = '" << sjis_str << "', ";

        utf8_str = res->getString("color");
        sjis_str = utf8_to_sjis(utf8_str);
        cout << "color = " << sjis_str << ", ";
        
        cout << "height = " << res->getDouble("height") << ", ";
        cout << "weight = " << res->getDouble("weight") << ", ";

        utf8_str = res->getString("type1");
        sjis_str = utf8_to_sjis(utf8_str);
        cout << "type1 = " << sjis_str << ", ";

        utf8_str = res->getString("type2");
        sjis_str = utf8_to_sjis(utf8_str);
        cout << "type2 = " << sjis_str << endl;
        
    }
    delete res;
}

void InsertType1Data(Connection* con, Statement* stmt, char *fname1)
{
    FILE* fp;
    if ((fp = fopen(fname1, "r")) == NULL) {
        return;
    }
    else 
    {
        stmt->execute("CREATE TABLE Type1(type_num1 int PRIMARY KEY, \
                                          type1 varchar(10))");
        cout << "\" Type1 \" table has been created." << endl;

        char s[BUFFERSIZE] = "";
        char* ptr[2 + 1];
        PreparedStatement* pstmt = con->prepareStatement("INSERT INTO Type1(type_num1, type1) VALUES(?,?)");

        while (fgets(s, BUFFERSIZE, fp) != NULL) {
            s[strlen(s) - 1] = '\0'; //'\n' -> '\0'

            ptr[0] = strtok(s, " "); //split to each element per ' '(space)
            for (int i = 1; ptr[i - 1] != NULL; i++) { ptr[i] = strtok(NULL, " "); }

            string utf8_str = ptr[1];
            pstmt->setInt(1, atoi(ptr[0])); //type_num
            pstmt->setString(2, utf8_str);  //type
            pstmt->execute();
        }
        delete pstmt;
    }
}

void InsertPokemonData(Connection* con, Statement* stmt, char* fname3)
{
    FILE* fp;
    if ((fp = fopen(fname3, "r")) == NULL) {
        return;
    }
    else 
    {
        stmt->execute("CREATE TABLE Pokemon(num int PRIMARY KEY, \
                                            name varchar(10), \
                                            color_num int, \
                                            height double, \
                                            weight double, \
                                            type_num1 int, \
                                            type_num2 int, \
                                            FOREIGN KEY(color_num) REFERENCES Color(color_num), \
                                            FOREIGN KEY(type_num1) REFERENCES Type1(type_num1), \
                                            FOREIGN KEY(type_num2) REFERENCES Type2(type_num2))");
        
        cout << "\" Pokemon \" table has been created." << endl;

        char s[BUFFERSIZE] = "";
        char* ptr[7 + 1];
        PreparedStatement* pstmt;
        pstmt = con->prepareStatement("INSERT INTO Pokemon(num, name, color_num, height, weight, type_num1, type_num2) \
                                                           VALUES(?,?,?,?,?,?,?)");

        while (fgets(s, BUFFERSIZE, fp) != NULL) {
            s[strlen(s) - 1] = '\0'; //'\n' to '\0'

            ptr[0] = strtok(s, " "); //split to each element per ' '(space)
            for (int i = 1; ptr[i - 1] != NULL; i++) ptr[i] = strtok(NULL, " ");
            
            string sjis_str = ptr[1];
            string utf8_str = sjis_to_utf8(sjis_str);
           
            pstmt->setInt(1, atoi(ptr[0]));    //num
            pstmt->setString(2, utf8_str);     //name
            pstmt->setInt(3, atoi(ptr[2]));    //color
            pstmt->setDouble(4, atof(ptr[3])); //height
            pstmt->setDouble(5, atof(ptr[4])); //weight
            pstmt->setInt(6, atoi(ptr[5]));    //type1
            pstmt->setInt(7, atoi(ptr[6]));    //type2
            pstmt->execute();
        }
        delete pstmt;
    }
}

void InsertType2Data(Connection* con, Statement* stmt, char *fname1)
{
    FILE* fp;
    if ((fp = fopen(fname1, "r")) == NULL) {
        return;
    }
    else
    {
        stmt->execute("CREATE TABLE Type2(type_num2 int PRIMARY KEY, \
                                          type2 varchar(10))");
        cout << "\" Type2 \" table has been created." << endl;

        char s[BUFFERSIZE] = "";
        char* ptr[2 + 1];
        PreparedStatement* pstmt = con->prepareStatement("INSERT INTO Type2(type_num2, type2) VALUES(?,?)");

        while (fgets(s, BUFFERSIZE, fp) != NULL) {
            s[strlen(s) - 1] = '\0'; //'\n' -> '\0'
            
            ptr[0] = strtok(s, " "); //split to each element per ' '(space)
            for (int i = 1; ptr[i - 1] != NULL; i++) { ptr[i] = strtok(NULL, " "); }
          
            string utf8_str = ptr[1];
            pstmt->setInt(1, atoi(ptr[0])); //type_num
            pstmt->setString(2, utf8_str);  //type
            pstmt->execute();
        }
        delete pstmt;
    }
}

void CheckType1Data(Statement* stmt)
{
    ResultSet* res = (stmt->executeQuery("SELECT * FROM Type1"));
 
    while (res->next())
    {
        cout << row << ": ";
        cout << "type_num1. " << res->getInt("type_num1") << ", ";
        string utf8_str = res->getString("type1");
        string sjis_str = utf8_to_sjis(utf8_str);
        cout << "type_num1 = " << sjis_str << endl;
    }
    delete res;
}

void CheckType2Data(Statement* stmt)
{
    ResultSet* res = (stmt->executeQuery("SELECT * FROM Type2"));
    while (res->next())
    {
        cout << "type_num2. " << res->getInt("type_num2") << ", ";
        string utf8_str = res->getString("type2");
        string sjis_str = utf8_to_sjis(utf8_str);
        cout << "type_num2 = " << sjis_str << endl;
    }
    delete res;
}

void CheckPokemonData(Statement* stmt) 
{
    ResultSet* res = (stmt->executeQuery("SELECT * FROM Pokemon"));

    while (res->next()) 
    {
        cout << "No. " << res->getInt("num") << ", ";
        string utf8_str = res->getString("name");
        string sjis_str = utf8_to_sjis(utf8_str);  
        cout << "name = '" << sjis_str << "', ";
       
        cout << "color= " << res->getInt("color_num") << ", ";
        cout << "height = " << res->getDouble("height") << ", ";
        cout << "weight = " << res->getDouble("weight") << ", ";
        cout << "type1 = " << res->getInt("type_num1") << ",";
        cout << "type2 = " << res->getInt("type_num2") << endl;

    }
    delete res;
}

void CheckColourData(Statement* stmt)
{
    ResultSet* res = (stmt->executeQuery("SELECT * FROM Color"));

    while (res->next())
    {
        cout << "color_num. " << res->getInt("color_num") << ", ";
        string utf8_str = res->getString("color");
        string sjis_str = utf8_to_sjis(utf8_str);
        cout << "color = " << sjis_str << endl;
    }
    delete res;
}

void InsertColourData(Connection* con, Statement* stmt, char *fname2)
{
    FILE* fp;
    if ((fp = fopen(fname2, "r")) == NULL) {
        return;
    }
    else 
    {
        stmt->execute("CREATE TABLE Color(color_num int PRIMARY KEY, \
                                          color varchar(10))");
        cout << "\" Color \" table has been created." << endl;

        char s[BUFFERSIZE] = "";
        char* ptr[2 + 1];
        PreparedStatement* pstmt = con->prepareStatement("INSERT INTO Color(color_num, color) VALUES(?,?)");

        while (fgets(s, BUFFERSIZE, fp) != NULL) {
            s[strlen(s) - 1] = '\0'; //'\n' -> '\0'
            
            ptr[0] = strtok(s, " "); //split to each element per ' '(space)
            for (int i = 1; ptr[i - 1] != NULL; i++) { ptr[i] = strtok(NULL, " "); }

            string utf8_str = ptr[1];
            pstmt->setInt(1, atoi(ptr[0])); //color_num
            pstmt->setString(2, utf8_str);  //color
            pstmt->execute();
        }
        delete pstmt;
    }
}

void DeleteAllTableOrView(Statement* stmt, string DATABASE)
{
    stmt->execute("USE " + DATABASE);
    stmt->execute("DROP VIEW IF EXISTS PokeVIEW");
    stmt->execute("DROP TABLE IF EXISTS Pokemon");
    stmt->execute("DROP TABLE IF EXISTS Type1");
    stmt->execute("DROP TABLE IF EXISTS Type2");
    stmt->execute("DROP TABLE IF EXISTS Color");
}