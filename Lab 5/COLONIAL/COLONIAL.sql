CREATE TABLE Participant (
ParticipantNumber INTEGER PRIMARY KEY,
LastName CHAR(20) NOT NULL,
FirstName CHAR(20),
Address CHAR(50),
City CHAR(20),
State CHAR(2),
PostalCode CHAR(4),
TelephoneNumber CHAR(11),
DateOfBirth DATE
);

CREATE TABLE AdventureClass (
ClassNumber INT PRIMARY KEY,
Description CHAR(100),
MaxParticipants INT,
Fee DECIMAL(10,2),
);

CREATE TABLE ParticipantEnrollment (
ParticipantNumber INT,
ClassNumber INT,
EnrollmentDate DATETIME,
FOREIGN KEY (ParticipantNumber) REFERENCES Participant(ParticipantNumber)
FOREIGN KEY (ClassNumber) REFERENCES AdventureClass(ClassNumber)
);

CREATE TABLE ClassRoster (
ClassNumber INT,
ClassDate DATETIME,
ParticipantNumber INT,
FOREIGN KEY (ClassNumber) REFERENCES AdventureClass(ClassNumber)
FOREIGN KEY (ParticipantNumber) REFERENCES Participant(ParticipantNumber)
);
