# Apartment.py

class Apartment:
    def __init__(self, rent=0, metersFromUCSB=0, condition="N/A"):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}" \
                .format(self.rent, self.metersFromUCSB, self.condition)


    def __lt__(self, other):
        if self.rent < other.rent:
            return True
        elif self.rent > other.rent:
            return False
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB > other.metersFromUCSB:
                return False
            elif self.metersFromUCSB == other.metersFromUCSB:

                if self.condition == 'excellent' and other.condition == 'excellent':
                    return False
                elif self.condition == 'excellent' and other.condition == 'average':
                    return True
                elif self.condition == 'excellent' and other.condition == 'bad':
                    return True
                elif self.condition == 'average' and other.condition == 'excellent':
                    return False
                elif self.condition == 'average' and other.condition == 'average':
                    return False
                elif self.condition == 'average' and other.condition == 'bad':
                    return True
                elif self.condition == 'bad' and other.condition == 'excellent':
                    return False
                elif self.condition == 'bad' and other.condition == 'average':
                    return False
                elif self.condition == 'bad' and other.condition == 'bad':
                    return False

    def __ge__(self, other):
        if self.rent > other.rent:
            return True
        elif self.rent < other.rent:
            return False
        elif self.rent == other.rent:
            if self.metersFromUCSB > other.metersFromUCSB:
                return True
            elif self.metersFromUCSB < other.metersFromUCSB:
                return False
            elif self.metersFromUCSB == other.metersFromUCSB:

                if self.condition == 'excellent' and other.condition == 'excellent':
                    return False
                elif self.condition == 'excellent' and other.condition == 'average':
                    return False
                elif self.condition == 'excellent' and other.condition == 'bad':
                    return False
                elif self.condition == 'average' and other.condition == 'excellent':
                    return True
                elif self.condition == 'average' and other.condition == 'average':
                    return False
                elif self.condition == 'average' and other.condition == 'bad':
                    return False
                elif self.condition == 'bad' and other.condition == 'excellent':
                    return True
                elif self.condition == 'bad' and other.condition == 'average':
                    return True
                elif self.condition == 'bad' and other.condition == 'bad':
                    return False

    def __eq__(self, other):
        if self.rent < other.rent:
            return False
        elif self.rent < other.rent:
            return False
        else:
            if self.metersFromUCSB > other.metersFromUCSB:
                return False
            elif self.metersFromUCSB < other.metersFromUCSB:
                return False
            else:
                if self.condition == 'excellent' and other.condition == 'excellent':
                    return True
                elif self.condition == 'excellent' and other.condition == 'average':
                    return False
                elif self.condition == 'excellent' and other.condition == 'bad':
                    return False
                elif self.condition == 'average' and other.condition == 'excellent':
                    return True
                elif self.condition == 'average' and other.condition == 'average':
                    return True
                elif self.condition == 'bad' and other.condition == 'excellent':
                    return True
                elif self.condition == 'bad' and other.condition == 'average':
                    return True
                elif self.condition == 'bad' and other.condition == 'bad':
                    return True


