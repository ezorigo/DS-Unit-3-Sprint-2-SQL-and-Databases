import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()

query = """
    SELECT ProductName, UnitPrice
    FROM Product
    ORDER BY UnitPrice DESC LIMIT 10;
"""

query1 = """
    SELECT AVG(julianday(HireDate) - julianday(BirthDate))/ 365.2
    FROM Employee;
"""

query2 = """
    SELECT AVG(julianday(HireDate) - julianday(BirthDate))/ 365.2 as avg_age,
    City
    FROM Employee
    GROUP BY City;
"""

query3 = """
    SELECT ProductName, UnitPrice, CompanyName 
    FROM Product JOIN Supplier on Supplier.Id = SupplierId
    ORDER BY UnitPrice DESC LIMIT 10;
"""

query4 = """
    SELECT CategoryName, COUNT(CategoryId) as count
    FROM Product
    JOIN Category ON Category.Id = CategoryId
    GROUP BY CategoryId
    ORDER BY count DESC LIMIT 10;
"""

query5 = """
    SELECT LastName, FirstName, COUNT(DISTINCT TerritoryId)
    FROM Employee
    JOIN EmployeeTerritory ON Employee.Id = EmployeeId
    GROUP BY EmployeeId
    ORDER BY COUNT(DISTINCT TerritoryId) DESC
    LIMIT 1;
"""

print("Part 2")
print("1. " + str(curs.execute(query).fetchall()))
print("2. " + str(curs.execute(query1).fetchall()))
print("3. " + str(curs.execute(query2).fetchall()))
print("Part 3")
print("1. " + str(curs.execute(query3).fetchall()))
print("2. " + str(curs.execute(query4).fetchall()))
print("3. " + str(curs.execute(query5).fetchall()))

curs.close()
conn.commit()
