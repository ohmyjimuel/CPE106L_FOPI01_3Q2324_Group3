CREATE TABLE Renter (
RenterNumber INT PRIMARY KEY,
FirstName CHAR(20),
MiddleInitial CHAR(2),
LastName CHAR(20),
Address CHAR(50),
City CHAR(20),
State CHAR(2),
PostalCode CHAR(4),
TelephoneNumber CHAR(11), 
EmailAddress CHAR(30),
);

CREATE TABLE Property (
LocationNumber INT PRIMARY KEY,
LocationName CHAR(30),
Address CHAR(50),
City CHAR(20)
State CHAR(2),
PostalCode CHAR(4),
UnitNumber CHAR(3),
SquareFootage DECIMAL(10,2),
NumBedrooms INT,
NumBathrooms INT,
MaxSleepCapacity INT,
WeeklyRate DECIMAL(10,2),
);

CREATE TABLE RentalAgreement (
RenterNumber INT,
FirstName CHAR(20),
MiddleInitial CHAR(2),
LastName CHAR(20),
Address CHAR(50),
City CHAR(20),
State CHAR(2),
PostalCode CHAR(4),
TelephoneNumber CHAR(11),
StartDate DATE,
EndDate DATE,
WeeklyRentalAmount DECIMAL(10,2),
FOREIGN KEY (RenterNumber) REFERENCES Property(RenterNumber)
);

