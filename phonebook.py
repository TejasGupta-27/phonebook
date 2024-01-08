import csv 



class PhoneRecord:
    def __init__(self, name, organisation, phone_numbers):
        self.name = name
        self.organisation = organisation
        self.phone_numbers = phone_numbers

    def get_name(self):
        return self.name

    def get_organisation(self):
        return self.organisation

    def get_phone_numbers(self):
        return self.phone_numbers

class HashTableRecord:
    def __init__(self, key, record):
        self.key = key
        self.record = record
        self.next = None

    def get_key(self):
        return self.key

    def get_record(self):
        return self.record

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt


class PhoneBook:
    HASH_TABLE_SIZE = 263


    def __init__(self):
        self.hash_table = [None] * PhoneBook.HASH_TABLE_SIZE


    def create_phone_record(self, contact_info):
        name, num, org = contact_info.split(",")
        return PhoneRecord(name.strip(), org.strip(), [num.strip()])

    def compute_hash(self, string):
        tempsum=0
        for i in range(len(string)):
            tempsum+=ord(string[i])*((263**i)%1000000007)
        return(tempsum%263)
        # Implement a hash function for strings
        # You can use Python's built-in hash function or implement a custom one

        
        
    def add_contact(self, record):
        key=self.compute_hash(record.get_name())
        current=self.hash_table[key]
        if self.hash_table[key] is not None:
            while current.get_next() is not None:
                current=current.get_next()
            current.set_next(HashTableRecord(key,record)) 
            
        else:
            
            self.hash_table[key]=HashTableRecord(key,record)     
               
        # Implement adding a contact to the phone book
        # You need to compute the hash for the record's name and insert it into the hash table
        return
    def delete_contact(self, name):
        result=self.fetch_contacts(name)
        if (len(result)==0):

            return False
        
        for i in self.hash_table:
            if i is not None:
                key=i.get_key()
                current=i
                if i.get_record()==result[0]:
                     
                    self.hash_table[key] =None

                    return True
                

                while current is not None :
                    next=current.get_next()
                    if(next is not None and next.get_record()==result[0]):
                        current.set_next(next.get_next())
                        return True
                    current=next
        return False
 
        # Implement deleting a contact from the phone book
        # You need to find the record with the given name and remove it from the hash table
    def fetch_contacts(self, query):
        Names=query.split()
        
        result = []
        # for i in Names:
            
        for i in  Names:
            for j in self.hash_table:
                if j is not None:
                    current=j
                    while current is not None:
                        z=current.get_record().get_name()
                        if i in z:
                            result.append(current.get_record())
                        current=current.get_next()    
                                                             
        result=sorted(result,key=result.count,reverse=True)

        # Implement fetching contacts based on the query
        # You may need to split the query into words and hash them separately
        # Then, retrieve and merge the records from the appropriate hash table slots
        # Sort and return the merged records
        
        return result
    def read_records_from_file(self,file):
        with open(file) as csv_file:
            csv_reader=csv.reader(csv_file,delimiter='\n')
                    
            
            for i in csv_reader:                
                for j in i:
                    
                    print("\n")
                    
                    x=j.split(",")
                    # print(x)
                
                    Name=x[0]

                    
                    Phone_Object = PhoneRecord(Name,x[-1],x[1:-1])
                    # print(Phone_Object.get_name(),self.compute_hash(Phone_Object.get_name()))
                    
                        
                    self.add_contact(Phone_Object)
           
                 
# x=PhoneBook()
# x.read_records_from_file("Details.txt")
# y=PhoneRecord('Tejas',"yo",94040)
# x.add_contact(y)
# print(x.fetch_contacts("Tejas"))
# print(x.delete_contact("Tejas"))
# print(x.fetch_contacts("Tejas"))

