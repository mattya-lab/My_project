#pragma once
#pragma warning(disable : 4996)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <iostream>
#include <string>

#include <mysql_driver.h>
#include <mysql_connection.h>
#include <mysql_error.h>
#include <cppconn/Statement.h>
#include <cppconn/ResultSet.h>
#include <cppconn/prepared_statement.h>

#include "CreateAllTable.h"

using namespace std;
using namespace sql;

#define BUFFERSIZE (255)
#define rep(i, n) for(int i = 0; i < n; i++)

//---------------------------------------------------------------
const string HOST = "tcp://127.0.0.1:3306";
const string USER = "root";
const string PASSWORD = "";
const string DATABASE = "mysql";

char fname1[BUFFERSIZE] = "type.txt";
char fname2[BUFFERSIZE] = "color.txt";
char fname3[BUFFERSIZE] = "pokemon.txt";

int color = 0;
double height = 0.0, weight = 0.0;
//-------------------------------------------------------

void CreateView(Statement* stmt);

int main(void)
{
    try {
        Driver* driver = get_driver_instance();
        Connection* con = driver->connect(HOST, USER, PASSWORD);
        Statement* stmt = con->createStatement();
       
        DeleteAllTableOrView(stmt, DATABASE);
        
        InsertType1Data(con, stmt, fname1);
        //CheckType1Data(stmt);
        
        InsertType2Data(con, stmt, fname1);
        //CheckType2Data(stmt);
       
        InsertColourData(con, stmt, fname2);
        //CheckColourData(stmt);
        
        InsertPokemonData(con, stmt, fname3);
        //CheckPokemonData(stmt);
        
     
        CreateView(stmt);
        CheckTotalTable(stmt);
        cout << "Create view" << endl;

        delete con;
        delete stmt;
    }
    catch (SQLException & e) { return EXIT_FAILURE; }
    catch (runtime_error & e) { return EXIT_FAILURE; }
    
    return 0;
}

void CreateView(Statement* stmt) 
{
    stmt->execute("CREATE VIEW PokeVIEW AS\
                   SELECT Pokemon.num, \
                          Pokemon.name, \
                          Color.color, \
                          Pokemon.height,\
                          Pokemon.weight, \
                          Type1.type1, \
                          Type2.type2 \
                   FROM Pokemon \
                   INNER JOIN Color ON Pokemon.color_num = Color.color_num \
                   INNER JOIN Type1 ON Pokemon.type_num1 = Type1.type_num1 \
                   INNER JOIN Type2 ON Pokemon.type_num2 = Type2.type_num2 \
                   ORDER BY Pokemon.num");

    cout << "Create View" << endl;
}