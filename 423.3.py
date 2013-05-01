# Problem 423

# This is a program to keep track of conference attendees


class conferenceAttendee:

    def __init__(self, name, company, state, email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def getName(self):
        return self.name

    def getCompany(self):
        return self.company

    def getState(self):
        return self.state

    def getEmail(self):
        return self.email

    def displayNameEmail(self):
        print (self.getName(), self.getEmail())

class conferenceAttendees:

    def __init__(self):
        self.attendeesList = []
        infile = open("ConferenceAttendees", "r")
        for line in infile:
            items = line.split()
            firstName = str(items[0])
            lastName = str(items[1])
            name = firstName + " " + lastName
            company = str(items[2])
            state = str(items[3])
            email = str(items[4])
            attendee = conferenceAttendee(name, company, state, email)
            self.attendeesList.append(attendee)

    def addAttendee(self, attendee):
        self.attendeesList.append(attendee)

    def deleteAttendee(self, name):
        for attendee in self.attendeesList:
            if attendee.getName() == name:
                self.attendeesList.remove(attendee)

    def displayInfo(self, name):
        for attendee in self.attendeesList:
            if attendee.getName() == name:
                print (attendee.getName(), attendee.getCompany(), attendee.getState(), attendee.getEmail())

    def displayAllNamesEmails(self):
        for object in self.attendeesList:
            object.displayNameEmail()

    def displayAllNamesEmailsfromState(self, state):
        for object in self.attendeesList:
            if object.getState() == state:
                object.displayNameEmail()

    def printInfoToFile(self):
        outfile = open("ConferenceAttendees", "w")
        for object in self.attendeesList:
            print (object.getName(), object.getCompany(), object.getState(), object.getEmail(), file = outfile)
        outfile.close()

def printIntro():
    print ("This is a program to keep track of conference attendees in a file.")
    print ("Attendees are listed by name, company, state, and email.")
    print ()

def main ():

    printIntro()

    # create a list of attendees as an object
    attendees = conferenceAttendees()

    # first choice
    print ("To add an attendee, type 'add' (without quotation marks).")
    print ("To delete an attendee, type 'delete'.")
    print ("To display information on one attendee, type 'info'.")
    print ("To display the names and email addresses of all attendees, type 'display'.")
    print ("To display the names and email addresses of all attendees from a given state, type 'state'.")
    print ("To quit, hit the enter key.")
    print ()
    choice = input("Please enter a request from the above choices: ")
    print ()

    # choice loop
    while choice != "":
        if choice == 'add':
            name = input("Please enter the name of the attendee (with a space between first and last): ")
            company = input("Please enter the company name (with no spaces) of the attendee: ")
            state = input("Please enter the state that the attendee resides in (with no spaces): ")
            email = input("Please enter the email address of the attendee. ")
            attendee = conferenceAttendee(name, company, state, email)
            attendees.addAttendee(attendee)
        elif choice == 'delete':
            name = input("Please enter the name of the attendee (with a space between first and last): ")
            attendees.deleteAttendee(name)
        elif choice == 'info':
            name = input("Please enter the name of the attendee (with a space between first and last): ")
            attendees.displayInfo(name)
        elif choice == 'display':
            attendees.displayAllNamesEmails()
        else:
            state = input("Please enter the name of the state: ")
            attendees.displayAllNamesEmailsfromState(state)
        print ()
        choice = input("Please enter another request from the choices listed (or <enter> to quit): ")

    # print info to file
    attendees.printInfoToFile()

if __name__ == "__main__":
    main ()