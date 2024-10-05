import random
import pandas as pd 
def generate_usernames(name):
  """Generates a list of potential usernames based on a given name."""
  usernames = []
  usernames.append(name.lower())
  usernames.append(name.lower() + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_" + name.lower())
  usernames.append(name[0].lower() + name.lower())
  usernames.append(name.lower() + str(random.randint(10, 99)))
  usernames.append(name.lower() + "." + name.lower())
  usernames.append(name.lower() + str(random.randint(1, 9)) + name[0].lower())
  usernames.append(name.lower() + "_" + str(random.randint(1, 99)))
  usernames.append(name.lower() + "_" + name[0].lower() + str(random.randint(1, 9)))
  usernames.append(name[0].lower() + "." + name.lower())
  usernames.append(name.lower() + str(random.randint(2000, 2025)))
  usernames.append(name.lower() + "_user")
  usernames.append("user_" + name.lower())
  usernames.append(name.lower() + str(random.randint(1000, 9999)))
  usernames.append(name.lower() + "x" + name.lower())
  usernames.append(name.lower() + str(random.randint(50, 99)) + "x")
  usernames.append(name.lower() + "_" + str(random.randint(100, 999)))
  usernames.append("x" + name.lower() + "x")
  usernames.append(name[0].lower() + "_" + name.lower())
  usernames.append("x_" + name.lower())
  usernames.append(name.lower() + "_official")
  usernames.append("official_" + name.lower())
  usernames.append(name.lower()+ "official_")
  usernames.append(name.lower()+ "official_" + name[0])
  usernames.append(name.lower() + "_x" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_" + str(random.randint(20, 50)))
  usernames.append(name.lower() + name[0].lower() + str(random.randint(10, 99)))
  usernames.append(name.lower() + "xx")
  usernames.append(name[0].lower() + name.lower() + str(random.randint(100, 999)))
  usernames.append(name.lower() + "." + name[0].lower() + str(random.randint(1, 9)))
  usernames.append(name.lower() + str(random.randint(1, 9)) + "_" + name.lower())
  usernames.append("user_" + name.lower() + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_xyz")
  usernames.append(name[0].lower() + str(random.randint(100, 999)) + name.lower())
  usernames.append(name.lower() + "_" + name.lower() + str(random.randint(1, 9)))
  usernames.append(name[0].lower() + name.lower() + "_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_abc")
  usernames.append("abc_" + name.lower())
  usernames.append(name.lower() + "_123")
  usernames.append("xyz_" + name.lower())
  usernames.append(name.lower() + str(random.randint(100, 999)) + "_x")
  usernames.append(name.lower() + "." + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_xyz_" + str(random.randint(1, 9)))
  usernames.append("the_" + name.lower())
  usernames.append(name.lower() + "_xx_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_x_" + name[0].lower() + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_pro_" + str(random.randint(1, 9)))
  usernames.append("xx_" + name.lower() + "_" + str(random.randint(100, 999)))
  usernames.append("super_" + name.lower())
  usernames.append(name.lower() + "_the_" + str(random.randint(10, 99)))
  usernames.append("i_am_" + name.lower())
  usernames.append("mr_" + name.lower())
  usernames.append("ms_" + name.lower())
  usernames.append("miss_" + name.lower())
  usernames.append("dr_" + name.lower())
  usernames.append("prof_" + name.lower())
  usernames.append(name.lower() + "_master_" + str(random.randint(10, 99)))
  usernames.append("x_" + name.lower() + "_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_extra")
  usernames.append(name.lower() + "_user_" + str(random.randint(1, 99)))
  usernames.append(name.lower() + str(random.randint(1, 9)) + "x" + name.lower())
  usernames.append(name.lower() + "_pro_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_" + name.lower() + "_official")
  usernames.append(name.lower() + "_hero_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_" + name[0].lower() + str(random.randint(10, 99)) + "_x")
  usernames.append(name.lower() + "_legend_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_" + name.lower() + "_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_king_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_queen_" + str(random.randint(10, 99)))
  usernames.append("x_" + name.lower() + str(random.randint(10, 99)) + "x")
  usernames.append(name.lower() + "_mvp_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_champ_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_alpha_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_omega_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + str(random.randint(1, 9)) + "_" + name.lower() + "x")
  usernames.append("xx_" + name.lower() + "_" + str(random.randint(10, 99)) + "_xx")
  usernames.append(name.lower() + "_xx_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_hero")
  usernames.append("hero_" + name.lower())
  usernames.append(name.lower() + "_max_" + str(random.randint(1, 9)))
  usernames.append("the_" + name.lower() + "_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + str(random.randint(10, 99)) + "_star")
  usernames.append(name.lower() + "_super_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_rocket_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_champion_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_pro_x_" + str(random.randint(100, 999)))
  usernames.append("x_" + name.lower() + "_" + name[0].lower())
  usernames.append(name.lower() + "_warrior_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_beast_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_ninja_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_elite_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_force_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_xx_" + str(random.randint(1, 9)) + "_x")
  usernames.append(name.lower() + "_star_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_elite_" + str(random.randint(100, 999)))
  usernames.append("the_" + name.lower() + "_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_hero_" + str(random.randint(100, 999)))
  usernames.append("master_" + name.lower() + "_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_champ_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_max_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_legend_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_ranger_" + str(random.randint(10, 99)))
  usernames.append("super_" + name.lower() + "_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_ninja_" + str(random.randint(100, 999)))
  usernames.append("x_" + name.lower() + "_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_wizard_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_commander_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_captain_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_sword_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_dragon_" + str(random.randint(100, 999)))
  usernames.append("hero_" + name.lower() + "_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_shadow_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_storm_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_thunder_" + str(random.randint(10, 99)))
  usernames.append("x_" + name.lower() + "_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_blaze_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_fury_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_phoenix_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_tiger_" + str(random.randint(1, 9)))
  usernames.append("warrior_" + name.lower() + "_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_strike_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_rebel_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_rider_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_guardian_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_phantom_" + str(random.randint(100, 999)))
  usernames.append("the_" + name.lower() + "_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_pioneer_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_viper_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_beast_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_titan_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_guardian_" + str(random.randint(100, 999)))
  usernames.append(name.lower() + "_shadow_" + str(random.randint(1, 9)))
  usernames.append("alpha_" + name.lower() + "_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_knight_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_storm_" + str(random.randint(100, 999)))
  usernames.append("master_" + name.lower() + "_" + str(random.randint(10, 99)))
  usernames.append(name.lower() + "_ninja_" + str(random.randint(1, 9)))
  usernames.append(name.lower() + "_king_" + str(random.randint(100, 999)))
  return usernames

names = [
    "John", "Mary", "Alex", "David", "Emily", "Michael", "Olivia", "William", "Ava", "Sophia",
    "Liam", "Noah", "Emma", "Isabella", "Mason", "James", "Benjamin", "Mia", "Charlotte", "Lucas",
    "Henry", "Amelia", "Elijah", "Harper", "Evelyn", "Ella", "Samuel", "Jackson", "Mila", "Scarlett",
    "Daniel", "Hannah", "Layla", "Ethan", "Chloe", "Avery", "Logan", "Luna", "Zoey", "Jacob",
    "Nora", "Riley", "Alexander", "Victoria", "Grace", "Gabriel", "Lucy", "Leo", "Hazel", "Isabelle",
    "Matthew", "Sofia", "Eleanor", "Carter", "Aria", "Penelope", "Levi", "Lily", "Zoe", "Wyatt",
    "Brooklyn", "Jack", "Savannah", "Sebastian", "Paisley", "Aiden", "Clara", "Madison", "Isaiah",
    "Aurora", "Caleb", "Elena", "Aaron", "Ellie", "Nathan", "Leah", "Connor", "Violet", "Stella",
    "Oliver", "Lucy", "Andrew", "Hazel", "Joshua", "Paisley", "Julian", "Sarah", "Luke", "Samantha",
    "Brayden", "Maya", "Owen", "Abigail", "Grayson", "Anna", "Lincoln", "Aria", "Hunter", "Serenity",
    "Christian", "Peyton", "Maverick", "Alice", "Roman", "Aubrey", "Jonathan", "Kennedy", "Anthony",
    "Addison", "Jameson", "Adeline", "Nicholas", "Madelyn", "Dominic", "Julia", "Eli", "Savannah",
    "Colton", "Caroline", "Ian", "Eva", "Miles", "Ruby", "Asher", "Everly", "Cameron", "Autumn",
    "Ezekiel", "Mackenzie", "Jayden", "Reagan", "Silas", "Eliana", "Adam", "Madeline", "Jose",
    "Isabelle", "Nolan", "Vivian", "Jeremiah", "Sophie", "Axel", "Ivy", "Easton", "Gianna", "Jaxon",
    "Valentina", "Kayden", "Clara", "Bennett", "Natalie", "Parker", "Aurora", "Weston", "Molly",
    "Everett", "Arianna", "Carson", "Jade", "Maddox", "Quinn", "Adrian", "Delilah", "Jordan",
    "Genesis", "Cooper", "Josephine", "Declan", "Malia", "Ryder", "Ariana", "Emmett", "Jocelyn",
    "Harrison", "Willow", "Sawyer", "Alyssa", "Jason", "Liliana", "Wyatt", "Elise", "Bentley",
    "Sienna", "Bryson", "Margaret", "Kingston", "Rylee", "Rowan", "Athena", "Braxton", "Evangeline",
    "Chase", "Cecilia", "Grant", "Lyla", "Theo", "Sloane", "Xander", "Genevieve", "Cody", "Brielle",
    "Tristan", "Camille", "Seth", "Daisy", "Griffin", "Paige", "Rhett", "Alana", "Holden", "Rose",
    "Arthur", "Amara", "Beckett", "Faith", "Colin", "Aspen", "Ronan", "Norah", "Brock", "Teagan",
    "Derek", "Holly", "Phoenix", "Laila", "Rafael", "Ruth", "Blake", "Rebecca", "Garrett", "Brianna",
    "Troy", "Alina", "Elliot", "Emery", "Finn", "Rowan", "Emerson", "Blakely", "Zion", "Alexandra",
    "Finnley", "Diana", "Marcus", "Esther", "Drake", "Phoebe", "Jasper", "Mira", "King", "Brynlee",
    "Caden", "Tessa", "Gage", "Maggie", "Dawson", "Julianna", "Maxwell", "Mckenna", "Zane", "Jada",
    "Holden", "Amaya", "Tanner", "Daniela", "Judah", "Alicia", "Kendrick", "Kayla", "Malcolm",
    "Nadia", "Walker", "Charlee", "Reed", "Jasmine", "Tucker", "Keira", "Quincy", "Maddison",
    "Cruz", "Adalynn", "Zachary", "Lucia", "Enzo", "Amira", "Abram", "Lucille", "Milo", "Alayna",
    "Romeo", "Gabriela", "Justice", "Aubree", "Rocco", "Lola", "Rhys", "Katherine", "Hugo", "Ayla",
    "Damien", "Raegan", "Porter", "Brynn", "Felix", "Kylee", "Hayes", "Elliana", "Erick", "Selena",
    "Harvey", "Kenzie", "Jude", "Francesca", "Zeke", "Leia", "Malachi", "Hallie", "Jett", "Lexi",
    "Colt", "Joanna", "Graham", "Parker", "Myles", "Dylan", "Jace", "Kevin", "Patrick", "Mason",
    "Nolan", "Reid", "Diego", "Maddox", "Oscar", "Matteo", "Tristan", "Landon", "Ryker", "Ryder",
    "Josiah", "Barrett", "Lorenzo", "Kaiden", "Ashton", "Jayce", "Dean", "Bodhi", "Beckett",
    "Dante", "Enrique", "Finley", "Griffin", "Sage", "Sawyer", "Santino", "Romeo", "Israel",
    "Raphael", "Conner", "August", "Emilio", "Leandro", "Caiden", "Gregory", "Spencer", "Andy",
    "Otto", "Quinn", "Ellis", "Jaxson", "Jonah", "Peter", "Damian", "Kai", "Riley", "Ryker",
    "Wesley", "Weston", "Zachariah", "Aiden", "Bradley", "Drew", "Emerson", "Holden", "Hudson",
    "Luca", "Luis", "Manuel", "Marcus", "Martin", "Max", "Raymond", "Richard", "Santiago", "Silas",
    "Simon", "Steven", "Thomas", "Timothy", "Victor", "Vincent", "Wesley", "Westin", "Zion",
    "Abraham", "Abel", "Bennett", "Brian", "Charlie", "Christian", "Clark", "Cody", "Colton",
    "Corey", "Cyrus", "David", "Davis", "Dexter", "Dominic", "Donovan", "Dorian", "Edward",
    "Emmanuel", "Francis", "Franklin", "Frederick", "George", "Gideon", "Grant", "Greyson", "Hank",
    "Harley", "Harold", "Harrison", "Hendrix", "Howard", "Ian", "Isaac", "Ivan", "Jack", "James",
    "Jared", "Jeffrey", "Jeremy", "Jesse", "John", "Jonathan", "Jordan", "Joseph", "Kane", "Karter",
    "Keegan", "Kendrick", "Khalil", "Kingston", "Kobe", "Kyle", "Lance", "Lawson", "Leo", "Leon",
    "Lincoln", "Logan", "Louis", "Maddox", "Malcolm", "Matias", "Matthew", "Maximus", "Maverick",
    "Miles", "Mitchell", "Moses", "Nathaniel", "Nehemiah", "Nicholas", "Nico", "Nikolai", "Noel",
    "Oliver", "Omar", "Oscar", "Pablo", "Patrick", "Paul", "Phoenix", "Quentin", "Rafael", "Ralph",
    "Raymond", "Reece", "Reed", "Reid", "Remy", "Richard", "Ricky", "Robert", "Rocco", "Ronald",
    "Rowan", "Russell", "Ryan", "Ryder", "Salvador", "Samuel", "Santino", "Sawyer", "Scott",
    "Sean", "Sebastian", "Silas", "Simon", "Skyler", "Sloan", "Spencer", "Sterling", "Stefan",
    "Stetson", "Steven", "Sullivan", "Tanner", "Tate", "Tatum", "Taylor", "Terry", "Thomas", "Tim",
    "Tobias", "Todd", "Tommy", "Tony", "Travis", "Trevor", "Tristan", "Troy", "Tyler", "Tyson",
    "Vincent", "Walker", "Walter", "Warren", "Wayne", "Wesley", "Weston", "William", "Wilson",
    "Wyatt", "Xander", "Xavier", "Zachary", "Zane","Aarav", "Aakash", "Abhay", "Aditya", "Ajay", "Akash", "Alok", "Aman", "Amit", "Amol",
    "Anand", "Anil", "Anirudh", "Ankit", "Ankur", "Arjun", "Arvind", "Ashish", "Ashok", "Atul",
    "Avinash", "Bharat", "Bhaskar", "Bhavesh", "Brijesh", "Chetan", "Chirag", "Deepak", "Dev", "Dhruv",
    "Dinesh", "Gaurav", "Girish", "Harish", "Harsh", "Hemant", "Hitesh", "Inder", "Indrajit", "Ishaan",
    "Jai", "Jitendra", "Kailash", "Karan", "Karthik", "Kishore", "Kunal", "Lakshman", "Lalit", "Lokesh",
    "Madhav", "Mahesh", "Manish", "Mayank", "Mohan", "Mukesh", "Nagaraj", "Naveen", "Nikhil", "Niraj",
    "Omkar", "Parth", "Pradeep", "Prakash", "Pranav", "Puneet", "Rahul", "Raj", "Rajan", "Rajeev",
    "Rajesh", "Rakesh", "Raman", "Ramesh", "Ravi", "Rohit", "Sachin", "Sandeep", "Sanjay", "Santosh",
    "Saurabh", "Shaan", "Shankar", "Sharad", "Shashi", "Shiv", "Shyam", "Siddharth", "Somesh", "Srinivas",
    "Subhash", "Sudhir", "Suhas", "Sumeet", "Sunil", "Suresh", "Tarun", "Uday", "Umesh", "Venkatesh",
    "Vikas", "Vikram", "Vinay", "Vineet", "Vishal", "Vivek", "Yash", "Yogesh",
    "Aadhya", "Aarohi", "Aarti", "Aasha", "Aditi", "Aishwarya", "Akanksha", "Alka", "Amrita", "Ananya",
    "Anika", "Anita", "Anjali", "Ankita", "Anshu", "Aparna", "Arpita", "Ashwini", "Ayesha", "Bhavana",
    "Chandni", "Charu", "Chhaya", "Damini", "Deepa", "Deepika", "Deepti", "Devika", "Diksha", "Divya",
    "Esha", "Gauri", "Gayatri", "Geeta", "Hema", "Indira", "Isha", "Jaya", "Jyoti", "Kajal",
    "Kamini", "Kanika", "Kavita", "Kiran", "Kirti", "Komal", "Lata", "Leela", "Lila", "Lina",
    "Madhuri", "Manisha", "Meena", "Megha", "Monika", "Naina", "Nalini", "Namita", "Nandini", "Neelam",
    "Neha", "Nikita", "Nisha", "Pallavi", "Parul", "Pooja", "Prachi", "Pragya", "Preeti", "Priya",
    "Radhika", "Rajani", "Rakhi", "Rekha", "Richa", "Riddhi", "Rina", "Ritu", "Riya", "Roshni",
    "Sakshi", "Sana", "Sangeeta", "Sanjana", "Sarita", "Seema", "Shalini", "Shikha", "Shilpa", "Shreya",
    "Shruti", "Smita", "Sneha", "Sonia", "Sonika", "Srishti", "Suman", "Sunita", "Sushma", "Swati",
    "Tanvi", "Tara", "Trisha", "Uma", "Urmila", "Vaishali", "Varsha", "Vidya", "Vijaya", "Yamini",
    "Zoya", "Akhil", "Alka", "Anshika", "Anupama", "Anusha", "Anvesha", "Aradhya", "Archana", "Aryan",
    "Bhagyashree", "Chitra", "Disha", "Divyansh", "Garima", "Gautam", "Ishita", "Jigyasa", "Kanika", "Kriti",
    "Lavanya", "Manasi", "Manya", "Medha", "Meher", "Mitali", "Muskan", "Nidhi", "Niranjan", "Pari",
    "Payal", "Pratyush", "Prisha", "Ragini", "Rajeshwari", "Rajshree", "Raksha", "Ramya", "Richa", "Ridhima",
    "Rishabh", "Sakshi", "Sanjana", "Sanya", "Sapna", "Sarika", "Shivangi", "Shraddha", "Siddhi", "Simran",
    "Sonal", "Supriya", "Tanisha", "Tejas", "Tushar", "Vaibhav", "Vani", "Varun", "Vedant", "Vibhuti",
    "Vikas", "Vrinda", "Yashvi", "Yogita", "Zarina", "Zoya", "Nayantara", "Nishant", "Anshuman", "Aditi",
    "Shantanu", "Amitabh", "Siddhartha", "Anushka", "Keshav", "Krishna", "Lakshmi", "Lalita", "Manoj", "Mira",
    "Nandita", "Nayak", "Nishtha", "Om", "Padma", "Pranali", "Rajiv", "Ram", "Reva", "Reyansh",
    "Rohan", "Roshan", "Sahil", "Samir", "Sandhya", "Santosh", "Saroj", "Shobha", "Shrikant", "Sonam",
    "Sudha", "Sunanda", "Suraj", "Teja", "Tilak", "Tina", "Trupti", "Uma", "Usha", "Vandana",
    "Veena", "Vijay", "Vimla", "Vinod", "Vishnu", "Yogendra", "Aarya", "Aastha", "Abhilash", "Abhijit",
    "Achal", "Adarsh", "Aditi", "Adrika", "Agnish", "Akriti", "Amanat", "Amar", "Amisha", "Amod",
    "Amrita", "Anandita", "Anika", "Anirudh", "Anjali", "Ankush", "Anmol", "Anoushka", "Anuj", "Anurag",
    "Anusha", "Aparajita", "Aravind", "Archit", "Arnav", "Arti", "Arvind", "Asha", "Ashok", "Asmita",
    "Ayesha", "Ayush", "Bhagya", "Bhaskar", "Bhavya", "Chaitanya", "Chandrakant", "Charvi", "Chetan", "Chinmay",
    "Damodar", "Darsh", "Darshan", "Deepak", "Deepali", "Deepti", "Devansh", "Devina", "Devraj", "Dhanya",
    "Dheeraj", "Dhvani", "Diksha", "Dipali", "Divit", "Durgesh", "Ekta", "Gauri", "Gautami", "Gautam",
    "Gayatri", "Geet", "Geeta", "Girish", "Gopal", "Harini", "Harsha", "Harshita", "Hemant", "Hemlata",
    "Hina", "Indira", "Ishani", "Ishita", "Jagat", "Jaspreet", "Jatin", "Jayant", "Jaya", "Jitendra",
    "Jyoti", "Kabir", "Kailash", "Kalpana", "Kalyani", "Kanchan", "Karan", "Karishma", "Karthik", "Kashish",
    "Kaushik", "Kavita", "Kavya", "Khushi", "Kirti", "Kiran", "Komal", "Kunal", "Lakshya", "Lalit",
    "Lavanya", "Leela", "Lina", "Lokesh", "Madhavi", "Madhuri", "Manisha", "Manju", "Manoj", "Manthan",
    "Mayuri", "Meenakshi", "Mohan", "Mukta", "Namrata", "Nandita", "Neeraj", "Neeta", "Neha", "Nidhi",
    "Nikesh", "Nilesh", "Nimisha", "Nina", "Niranjan", "Nirupama", "Nisha", "Nishant", "Nitesh", "Omkar",
    "Palak", "Pallavi", "Parvati", "Piyush", "Prachi", "Pragya", "Pranav", "Prashant", "Preeti", "Priya",
    "Priyanka", "Puja", "Punam", "Pushpa", "Radhika", "Rahul", "Raj", "Rajat", "Rajeev", "Rajesh",
    "Rakhi", "Ramesh", "Rani", "Ravi", "Rekha", "Richa", "Riddhi", "Rina", "Ritesh", "Ritu",
    "Rohit", "Roma", "Roshni", "Rupesh", "Sakshi", "Saloni", "Sanjana", "Sanjeev", "Sarika", "Sarla",
    "Sarthak", "Sashi", "Seema", "Shailesh", "Shalini", "Shama", "Shantanu", "Sharad", "Sharmila", "Shefali",
    "Shekar", "Shikha", "Shilpa", "Shiva", "Shraddha", "Shravan", "Shreya", "Shruti", "Siddharth", "Simran",
    "Sonal", "Sonia", "Sourabh", "Srinivas", "Srishti", "Sudhir", "Sujata", "Suman", "Sundar", "Sunil",
    "Suresh", "Surya", "Swati", "Tanvi", "Tanuja", "Tara", "Tina", "Tripti", "Uday", "Uma",
    "Upendra", "Urvashi", "Utkarsh", "Vaibhav", "Vandana", "Varsha", "Varun", "Veena", "Venkat", "Vikas",
    "Vikram", "Vimal", "Vinay", "Vineet", "Vinu", "Vipul", "Virendra", "Vishal", "Vishnu", "Vivek",
    "Yamini", "Yash", "Yogesh", "Yuvraj", "Zarina", "Zeenat","Li Wei", "Wang Fang", "Zhang Wei", "Liu Yang", "Chen Wei", "Yang Yue", "Zhao Lei", "Wu Jie", "Zhou Li", "Xu Wei",
    "Sun Yi", "Ma Li", "Hu Yan", "Guo Jing", "He Ping", "Gao Wei", "Lin Jie", "Luo Yan", "Huang Li", "Cao Lei",
    "Shen Yu", "Deng Jun", "Qian Yu", "Xia Lei", "Liu Ying", "Wang Lei", "Zhang Li", "Chen Ping", "Yang Ming", "Zhao Hui",
    "Wu Xia", "Zhou Wei", "Xu Yan", "Sun Lei", "Ma Wei", "Hu Li", "Guo Wei", "He Li", "Gao Lei", "Lin Li",
    "Luo Wei", "Huang Wei", "Cao Ping", "Shen Lei", "Deng Wei", "Qian Lei", "Xia Ping", "Liu Yan", "Wang Ying", "Zhang Ping",
    "Chen Ying", "Yang Wei", "Zhao Ming", "Wu Li", "Zhou Fang", "Xu Ying", "Sun Ping", "Ma Ming", "Hu Wei", "Guo Ming",
    "He Wei", "Gao Fang", "Lin Wei", "Luo Ying", "Huang Ping", "Cao Wei", "Shen Li", "Deng Ying", "Qian Wei", "Xia Li",
    "Liu Fang", "Wang Yan", "Zhang Hui", "Chen Hui", "Yang Xia", "Zhao Wei", "Wu Wei", "Zhou Ping", "Xu Ming", "Sun Fang",
    "Ma Fang", "Hu Ming", "Guo Fang", "He Ming", "Gao Yan", "Lin Fang", "Luo Fang", "Huang Yan", "Cao Ming", "Shen Fang",
    "Deng Li", "Qian Ming", "Xia Wei", "Liu Ming", "Wang Xia", "Zhang Yan", "Chen Xia", "Yang Ping", "Zhao Yan", "Wu Ming",
    "Zhou Ying", "Xu Xia", "Sun Yan", "Ma Yan", "Hu Ping", "Guo Yan", "He Yan", "Gao Ying", "Lin Yan", "Luo Ming",
    "Huang Ming", "Cao Yan", "Shen Ying", "Deng Fang", "Qian Yan", "Xia Fang", "Liu Wei", "Wang Ping", "Zhang Ming", "Chen Yan",
    "Yang Fang", "Zhao Fang", "Wu Yan", "Zhou Yan", "Xu Fang", "Sun Wei", "Ma Xia", "Hu Yan", "Guo Wei", "He Wei",
    "Gao Ming", "Lin Xia", "Luo Yan", "Huang Wei", "Cao Fang", "Shen Yan", "Deng Wei", "Qian Fang", "Xia Ying", "Liu Xia",
    "Wang Wei", "Zhang Xia", "Chen Fang", "Yang Wei", "Zhao Ying", "Wu Wei", "Zhou Xia", "Xu Yan", "Sun Wei", "Ma Wei",
    "Hu Fang", "Guo Fang", "He Xia", "Gao Wei", "Lin Wei", "Luo Xia", "Huang Yan", "Cao Wei", "Shen Wei", "Deng Yan",
    "Qian Wei", "Xia Yan", "Liu Wei", "Wang Fang", "Zhang Wei", "Chen Wei", "Yang Yan", "Zhao Xia", "Wu Yan", "Zhou Wei",
    "Xu Fang", "Sun Xia", "Ma Yan", "Hu Xia", "Guo Wei", "He Fang", "Gao Xia", "Lin Fang", "Luo Wei", "Huang Xia",
    "Cao Yan", "Shen Wei", "Deng Xia", "Qian Yan", "Xia Wei", "Liu Fang", "Wang Yan", "Zhang Xia", "Chen Yan", "Yang Wei",
    "Zhao Fang", "Wu Fang", "Zhou Yan", "Xu Xia", "Sun Yan", "Ma Fang", "Hu Yan", "Guo Fang", "He Yan", "Gao Wei",
    "Lin Yan", "Luo Fang", "Huang Yan", "Cao Wei", "Shen Fang", "Deng Yan", "Qian Wei", "Xia Yan", "Liu Wei", "Wang Xia",
    "Zhang Yan", "Chen Fang", "Yang Yan", "Zhao Yan", "Wu Wei", "Zhou Fang", "Xu Yan", "Sun Fang", "Ma Wei", "Hu Wei","Aleksandr", "Anastasia", "Andrei", "Anna", "Anton", "Arina", "Artem", "Boris", "Daria", "Dmitry",
    "Ekaterina", "Elena", "Evgeny", "Fyodor", "Galina", "Igor", "Inna", "Irina", "Ivan", "Kirill",
    "Konstantin", "Larisa", "Leonid", "Lidia", "Maksim", "Maria", "Marina", "Mikhail", "Natalia", "Nikita",
    "Nikolai", "Oksana", "Olga", "Pavel", "Polina", "Roman", "Sergey", "Sofiya", "Stanislav", "Svetlana",
    "Tatiana", "Timofey", "Vadim", "Valentina", "Valeria", "Vera", "Viktor", "Viktoria", "Vladimir", "Vladislav",
    "Yana", "Yaroslav", "Yelena", "Yulia", "Yuri", "Zoya", "Aleksey", "Alina", "Alyona", "Anatoly",
    "Angelina", "Anisa", "Arkadiy", "Artur", "Bogdan", "Danil", "Denis", "Diana", "Egor", "Galina",
    "Grigory", "Ilya", "Irina", "Karina", "Katerina", "Kristina", "Larisa", "Lidiya", "Lyudmila", "Margarita",
    "Mark", "Marta", "Matvey", "Mikhail", "Nadezhda", "Nikita", "Nikolay", "Nina", "Oleg", "Olesya",
    "Pavel", "Raisa", "Rostislav", "Semyon", "Sofiya", "Stanislav", "Stepan", "Svetlana", "Tamara", "Tatyana",
    "Timur", "Valentina", "Valentin", "Valeria", "Vasily", "Vera", "Veronika", "Viktor", "Viktoria", "Vladimir",
    "Vladislav", "Vyacheslav", "Yakov", "Yana", "Yaroslav", "Yelena", "Yelizaveta", "Yuliana", "Yuriy", "Zinaida",
    "Zlata", "Abram", "Agafya", "Aleksandrina", "Alexey", "Anfisa", "Anisim", "Arkhip", "Bogdana", "Borislav",
    "Danila", "Darina", "Demid", "Diana", "Dina", "Dmitri", "Dominika", "Efim", "Elizaveta", "Faina",
    "Fedor", "Filipp", "Grigory", "Ignat", "Ilona", "Innokentiy", "Ivan", "Izabella", "Kapitolina", "Klavdiya",
    "Klim", "Kristina", "Ksenia", "Leonid", "Lidiya", "Lina", "Lyubov", "Makar", "Marfa", "Marianna",
    "Miroslav", "Nadezhda", "Nailya", "Nastasya", "Nina", "Oksana", "Olga", "Petr", "Raisa", "Ruslan",
    "Sabina", "Semyon", "Snezhana", "Sofia", "Stepan", "Tamara", "Tatyana", "Timur", "Ulyana", "Ustin",
    "Vadim", "Valeria", "Vasilisa", "Veniamin", "Vera", "Veronika", "Viktoriya", "Vladimir", "Vladislav", "Vsevolod",
    "Yakov", "Yana", "Yaroslav", "Yaroslava", "Yelena", "Yelizaveta", "Yevgeniy", "Yulian", "Yulia", "Yuri",
    "Zahar", "Zinaida", "Zoya", "Alena", "Alfiya", "Amalia", "Anastasiya", "Andrey", "Antonina", "Arkadiy",
    "Artemiy", "Bogdan", "Daniil", "Evgeniya", "Faina", "Fyodor", "Galina", "Gennady", "Gleb", "Ilarion","Adolf", "Adelheid", "Adrian", "Agnes", "Albert", "Alexandra", "Alfred", "Alois", "Amalia", "Andreas",
    "Angela", "Anja", "Anna", "Anneliese", "Anton", "Arno", "Armin", "Artur", "Barbara", "Beate",
    "Bernd", "Bernhard", "Bettina", "Birgit", "Björn", "Brigitte", "Britta", "Bruno", "Carl", "Carla",
    "Carmen", "Carsten", "Christa", "Christian", "Christiane", "Christine", "Christopher", "Claudia", "Clemens", "Conrad",
    "Dagmar", "Daniel", "Daniela", "Dieter", "Dirk", "Doris", "Dorothea", "Eberhard", "Edeltraud", "Edgar",
    "Edith", "Edmund", "Eduard", "Elena", "Elisabeth", "Elmar", "Else", "Emil", "Emma", "Erich",
    "Erika", "Ernst", "Erwin", "Eva", "Felix", "Ferdinand", "Florian", "Franz", "Frederike", "Friedrich",
    "Fritz", "Georg", "Gerd", "Gerhard", "Gernot", "Gisela", "Gottfried", "Gregor", "Greta", "Günther",
    "Hanna", "Hans", "Harald", "Heike", "Heinrich", "Heinz", "Helena", "Helga", "Helmut", "Hermann",
    "Horst", "Hubert", "Hugo", "Inge", "Ingeborg", "Irene", "Iris", "Isabella", "Jan", "Jana",
    "Jens", "Jessica", "Joachim", "Johann", "Johanna", "Josef", "Judith", "Julia", "Julian", "Jürgen",
    "Karl", "Karin", "Karsten", "Katrin", "Klaus", "Konrad", "Kornelia", "Kurt", "Lars", "Laura",
    "Lea", "Leon", "Lena", "Leonhard", "Lothar", "Ludwig", "Lukas", "Magdalena", "Manfred", "Margarete",
    "Maria", "Marianne", "Marie", "Marina", "Markus", "Marlene", "Martin", "Matthias", "Max", "Maximilian",
    "Melanie", "Michael", "Monika", "Nadine", "Nico", "Nicole", "Norbert", "Olaf", "Oliver", "Otto",
    "Patricia", "Patrick", "Paul", "Petra", "Philipp", "Pia", "Ralf", "Rainer", "Reinhard", "Renate",
    "Richard", "Robert", "Roland", "Rolf", "Roswitha", "Rudolf", "Sabine", "Sandra", "Sascha", "Sebastian",
    "Silke", "Simon", "Simone", "Stefan", "Stefanie", "Susanne", "Sven", "Theodor", "Thomas", "Thorsten",
    "Tobias", "Ulrike", "Uwe", "Veronika", "Viktor", "Volker", "Walter", "Werner", "Wilhelm", "Wolfgang",
    "Yvonne", "Zoey", "Alexander", "Annika", "Bastian", "Benjamin", "Cornelia", "Dennis", "Elisa", "Franziska",
    "Gabi", "Gabriele", "Hans-Peter", "Heiko", "Janine", "Jörg", "Karl-Heinz", "Katharina", "Kirsten", "Kurt-Heinz",
    "Lena-Sophie", "Michaela", "Niklas", "Otmar", "Patrick", "Paulina", "Ralph", "Roland", "Siegfried", "Torsten",
    "Valentin", "Victoria", "Waldemar", "Winfried","Adriana", "Alejandro", "Alfonso", "Alma", "Alicia", "Andrés", "Ángel", "Ana", "Andrea", "Antonio",
    "Beatriz", "Benjamín", "Blanca", "Carlos", "Carmen", "Catalina", "Cristina", "David", "Dolores", "Eduardo",
    "Elena", "Elías", "Emilia", "Esteban", "Eva", "Fernando", "Francisco", "Gabriel", "Gloria", "Guillermo",
    "Helena", "Héctor", "Hilda", "Ignacio", "Isabel", "Iván", "Jaime", "Javier", "Jesús", "Jorge",
    "José", "José Antonio", "Juana", "Julia", "Julián", "Laura", "Luis", "Manuel", "María", "Mariana",
    "Mario", "Martín", "Mateo", "Marta", "Mercedes", "Miguel", "Montserrat", "Natalia", "Nicolás", "Noelia",
    "Óscar", "Patricia", "Pedro", "Raquel", "Rafael", "Ramón", "Raúl", "Ricardo", "Rosa", "Ruben",
    "Salvador", "Samuel", "Sandra", "Santiago", "Sara", "Sofía", "Sonia", "Teresa", "Tomás", "Valeria",
    "Vanessa", "Víctor", "Virginia", "Yolanda", "Zoe", "Alba", "Alicia", "Amelia", "Ana María", "Ángelica",
    "Antonio", "Aurelio", "Belén", "Benito", "Bernardo", "Blanca", "Bruno", "Carmen", "Carolina", "Celeste",
    "César", "Claudia", "Clemente", "Concepción", "Daniel", "Débora", "Diana", "Diego", "Domingo", "Eduarda",
    "Elisabeth", "Enrique", "Estela", "Eulalia", "Fabiola", "Felipe", "Francisca", "Gabriela", "Genaro", "Glenda",
    "Gregorio", "Guadalupe", "Héctor", "Hilda", "Inés", "Isabel", "Ivana", "Javier", "Joaquín", "José Luis",
    "Juan", "Juana", "Juventino", "Karina", "Karla", "Laura", "Leonor", "Leticia", "Lina", "Luis Miguel",
    "Manuel", "Marcela", "María José", "Mario", "Marisol", "Martha", "Martín", "Matías", "Mónica", "Natividad",
    "Néstor", "Noemi", "Ofelia", "Olga", "Oscar", "Paola", "Patricio", "Pedro", "Raúl", "Ramiro",
    "Renata", "Ricardo", "Rocío", "Rodrigo", "Rosario", "Rubén", "Ruth", "Sabina", "Salvador", "Santos",
    "Sergio", "Silvia", "Simón", "Sonia", "Teodoro", "Tomás", "Valeria", "Valentino", "Verónica", "Vicente",
    "Violeta", "Yadira", "Yolanda", "Adela", "Aitana", "Álvaro", "Araceli", "Aurelia", "Bárbara", "Belinda",
    "Blas", "Carmen", "Carla", "Clara", "Cristian", "Dalia", "Daniela", "Diana", "Efraín", "Elena",
    "Esteban", "Felicia", "Félix", "Fernanda", "Germán", "Guadalupe", "Hilda", "Isidoro", "Joaquín", "José Antonio",
    "Juan Carlos", "Julieta", "Lidia", "Luis Alberto", "Marcelo", "Mariana", "Mercedes", "Milagros", "Nora", "Patricio",
    "Ramona", "Rodolfo", "Rosa María", "Samantha", "Sandra", "Teodoro", "Valentina", "Vicente", "Virginia", "Yolanda",
    "Yulia", "Adriana", "Alejandra", "Álvaro", "Andrés", "Ana Paula", "Ángeles", "Antonio", "Araceli", "Ariel",
    "Benjamín", "Berta", "Carlos", "Catalina", "César", "Claudia", "Daniel", "Diana", "Dolores", "Eloísa",
    "Emilio", "Enrique", "Estela", "Eugenia", "Fabiola", "Félix", "Francisco", "Gabriela", "Gloria", "Héctor",
    "Iván", "Jaime", "Javier", "José Manuel", "Julián", "Karla", "Laura", "Leticia", "Luis", "María Teresa",
    "Marina", "Martín", "Marta", "Mercedes", "Miguel Ángel", "Montserrat", "Natalia", "Nicolás", "Noelia", "Óscar",
    "Patricia", "Pilar", "Rafael", "Raúl", "Ricardo", "Rosa", "Ruth", "Salvador", "Samuel", "Sandra",
    "Santiago", "Sara", "Silvia", "Sonia", "Teodoro", "Valeria", "Valentino", "Víctor", "Yolanda", "Zoe","Ahn", "Ari", "Bae", "Bang", "Baek", "Choi", "Chung", "Dong", "Eun", "Gim",
    "Hae", "Han", "Hee", "Hye", "Jang", "Jin", "Joo", "Kang", "Kim", "Lee",
    "Lim", "Park", "Ryu", "Shin", "Soo", "Song", "Woo", "Yoo", "Yun", "Yoon",
    "Ahn", "Bae", "Choi", "Chung", "Dong", "Eun", "Gim", "Han", "Hee", "Hye",
    "Jang", "Jin", "Joo", "Kang", "Kim", "Lee", "Lim", "Park", "Ryu", "Shin",
    "Soo", "Song", "Woo", "Yoo", "Yun", "Yoon", "Ahn Jae-hyun", "Bae Ji-won", "Choi Min-ho", "Choi Soo-jin",
    "Chung Hee-sun", "Dong Hoon", "Eun Young", "Gim Seok-jin", "Han Ji-min", "Hee Jin", "Hye Rin", "Jang Joon-ho",
    "Jin Ah", "Joo Hee", "Kang Hyun-woo", "Kim Ji-woo", "Lee Min-jung", "Lim Soo-hyun", "Park Ji-hoon", "Ryu Jin",
    "Shin Seung-ho", "Soo-kyung", "Song Hye-kyo", "Woo Seok", "Yoo Na", "Yun Ji-ho", "Yoon Seo-jin", "Ahn Soo-jin",
    "Bae Min-jun", "Choi Ji-hye", "Chung Ho", "Dong-joo", "Eun-ji", "Gim Jin-woo", "Han Yoon", "Hee-seo", "Hye-jin",
    "Jang Mi-na", "Jin-woo", "Joo-hyuk", "Kang Min-kyung", "Kim Sun-ho", "Lee Ji-eun", "Lim Jun-ho", "Park Min-sik",
    "Ryu Hae-young", "Shin Min-jae", "Soo-ah", "Song Jin-woo", "Woo-jin", "Yoo Kyung", "Yun Jae-woo", "Yoon Ji-eun",
    "Ahn Ji-ho", "Bae Seung-hyun", "Choi Ha-joon", "Choi Hyun-joo", "Chung Seo-jin", "Dong-sik", "Eun-mi", "Gim Yeon",
    "Han Joon", "Hee-joo", "Hye-ji", "Jang Na-ra", "Jin-hee", "Joo-sung", "Kang Ji-ho", "Kim Tae-hyun", "Lee Soo-bin",
    "Lim Hyun-ju", "Park Ji-hye", "Ryu Ji-won", "Shin Hye-jung", "Soo-yeon", "Song Ji-eun", "Woo Seung-min", "Yoo Jin",
    "Yun Hye-jin", "Yoon Seok-jin", "Ahn Sun-woo", "Bae Hae-jin", "Choi Eun-ji", "Choi Jae-sung", "Chung Min-jung",
    "Dong-wook", "Eun-seo", "Gim Hyun-jung", "Han Kyung", "Hee-young", "Hye-min", "Jang Seung-jae", "Jin-ah", "Joo-hwa",
    "Kang Hye-jin", "Kim Joon", "Lee Ji-ho", "Lim Hae-rim", "Park Sung-ho", "Ryu Sun-woo", "Shin Ji-hye", "Soo-jung",
    "Song Seung-hyun", "Woo Hyun-ji", "Yoo Seung-jae", "Yun Seung-jin", "Yoon Seung-woo", "Ahn Ji-yoon", "Bae Min-seo",
    "Choi Mi-sun", "Choi Sung-kyu", "Chung Ji-hoon", "Dong-kyung", "Eun-ha", "Gim Hyun-woo", "Han Min-jung", "Hee-rin",
    "Hye-jung", "Jang Ha-neul", "Jin-young", "Joo-sun", "Kang Ji-sung", "Kim Hae-jin", "Lee Hae-ji", "Lim Mi-na",
    "Park Hye-sun", "Ryu Ji-hye", "Shin Seok-jin", "Soo-min", "Song Hae-jin", "Woo Ji-hoon", "Yoo Seung-hye", "Yun Soo-jung",
    "Yoon Hyun-joo", "Ahn Hae-rin", "Bae Jae-min", "Choi Na-young", "Choi Seung-jae", "Chung Kyung-sun", "Dong-joon",
    "Eun-kyung", "Gim Kyung-sun", "Han Ji-eun", "Hee-sun", "Hye-jin", "Jang Soo-hyun", "Jin-kyung", "Joo-min", "Kang Hyun-suk",
    "Kim Jin-kyung", "Lee Min-seo", "Lim Seok-jin", "Park Seung-jae", "Ryu Hyun-suk", "Shin Min-seok", "Soo-hye", "Song Kyung-sun",
    "Woo Hae-young", "Yoo Hae-jin", "Yun Jin-kyung", "Yoon Hae-rin", "Ahn Seok-jin", "Bae Kyung-min", "Choi Joo-hyun",
    "Choi Min-jae", "Chung Sun-ho", "Dong-jung", "Eun-joo", "Gim Hae-young", "Han Hae-rin", "Hee-hye", "Hye-sun",
    "Jang Min-seo", "Jin-sun", "Joo-kyung", "Kang Hyun-joo", "Kim Seung-min", "Lee Hae-young", "Lim Ji-hye", "Park Ji-hyeon",
    "Ryu Kyung-sun", "Shin Hyun-joo", "Soo-seok", "Song Hae-kyung", "Woo Hae-jin", "Yoo Hyun-sun", "Yun Kyung-sun",
    "Yoon Min-seo", "Ahn Kyung-sun", "Bae Ji-hye", "Choi Min-ji", "Choi Hye-min", "Chung Mi-sun", "Dong-hyeok", "Eun-sun",
    "Gim Jin-seok", "Han Kyung-sun", "Hee-soo", "Hye-kyung", "Jang Kyung-sun", "Jin-min", "Joo-kyung", "Kang Kyung-ja",
    "Kim Hae-joo", "Lee Kyung-sun", "Lim Kyung-ja", "Park Min-jung", "Ryu Hye-min", "Shin Ji-sun", "Soo-kyung", "Song Hyun-seok",
    "Woo Hyun-woo", "Yoo Jin-sun", "Yun Hye-min", "Yoon Soo-hye", "Ahn Min-seo", "Bae Jin-sun", "Choi Seung-woo",
    "Choi Kyung-ja", "Chung Hae-rin", "Dong-hee", "Eun-min", "Gim Min-seo", "Han Mi-sun", "Hee-jung", "Hye-ji", "Jang Seung-jin",
    "Jin-min", "Joo-kyung", "Kang Hyun-seo", "Kim Seung-jae", "Lee Hae-kyung", "Lim Seung-woo", "Park Hae-kyung", "Ryu Min-jung",
    "Shin Seung-woo", "Soo-kyung", "Song Hye-min", "Woo Min-kyung", "Yoo Kyung-ja", "Yun Seung-woo", "Yoon Hae-jae","Akira", "Aoi", "Arisa", "Asahi", "Atsushi", "Ayaka", "Daiki", "Emi", "Eri", "Fumiko",
    "Haruka", "Hikari", "Hiroki", "Hitoshi", "Ichiro", "Izumi", "Jiro", "Jun", "Kaito", "Kana",
    "Kaneko", "Kaori", "Kazuhiro", "Keiko", "Kenji", "Kenta", "Kiku", "Koichi", "Kozue", "Mai",
    "Maki", "Manabu", "Mari", "Mariko", "Masato", "Mika", "Mikako", "Mio", "Miyuki", "Naoko",
    "Naruto", "Natsuki", "Nobu", "Nori", "Riko", "Ryo", "Ryota", "Saki", "Satoshi", "Sayaka",
    "Shin", "Shinya", "Shoko", "Sora", "Sosuke", "Takao", "Takuya", "Tamiko", "Taro", "Terumi",
    "Tetsuya", "Tomoko", "Toshi", "Yoko", "Yoshi", "Yoshiko", "Yuki", "Yumi", "Yusuke", "Aki",
    "Akemi", "Akiyo", "Atsuko", "Ayumi", "Chika", "Chiaki", "Chie", "Daisuke", "Eiko", "Fujiko",
    "Gen", "Goro", "Hana", "Haruki", "Hiro", "Hiroshi", "Hitomi", "Honoka", "Hoshi", "Ichika",
    "Ikumi", "Kazu", "Kei", "Ken", "Kie", "Kimiko", "Kiyoko", "Koji", "Kumiko", "Mao",
    "Masumi", "Mika", "Miki", "Mitsuki", "Miyako", "Nana", "Natsumi", "Nobuaki", "Noriko", "Rei",
    "Rina", "Ryohei", "Ryuki", "Sachi", "Satoru", "Shinji", "Shizuka", "Souta", "Sumire", "Takahiro",
    "Takumi", "Tamao", "Tomo", "Tomomi", "Toshiro", "Wataru", "Yasuo", "Yoko", "Yoshihiro", "Yuji",
    "Yuka", "Yuko", "Yusaku", "Yuuka", "Aoi", "Asuka", "Chiyo", "Etsuko", "Haru", "Haruto", "Hikaru",
    "Hiro", "Hiroko", "Ichiro", "Ikeda", "Jin", "Kanae", "Kaoru", "Keiichi", "Kenta", "Kie",
    "Kouki", "Kumi", "Mai", "Manami", "Marina", "Masa", "Masaki", "Miki", "Misaki", "Miyu",
    "Nami", "Nina", "Nobuhiro", "Noriaki", "Rena", "Rei", "Ryoichi", "Ryoko", "Sachi", "Sakura",
    "Satomi", "Shige", "Shinichi", "Sora", "Taka", "Takumi", "Tamaki", "Tomo", "Yoko", "Yoshie",
    "Yu", "Yuichi", "Yukari", "Yuki", "Yumi", "Yuriko", "Atsushi", "Chika", "Daisuke", "Eiko", "Fumi",
    "Hanae", "Haru", "Hidemi", "Ikumi", "Kaname", "Kei", "Kie", "Kiki", "Maki", "Mieko",
    "Miyuki", "Nana", "Naomi", "Natsumi", "Riko", "Ryo", "Sakura", "Shizuka", "Shun", "Sumi",
    "Takumi", "Taro", "Tatsu", "Tomomi", "Yoshiko", "Yumi", "Yuko", "Yuki", "Akio", "Ayaka",
    "Hikaru", "Hiroshi", "Junko", "Kazu", "Kazuki", "Kie", "Koji", "Mio", "Miyako", "Nari",
    "Natsuki", "Ryohei", "Ryuji", "Sachi", "Satoshi", "Shinobu", "Sora", "Sumire", "Takumi", "Tomo",
    "Yoshiko", "Yukio", "Yuri"
]

# Function to add years, numbers, and surnames to some names
def modify_name(name):
    if random.random() < 0.3:  # 30% chance to modify the name
        suffix_type = random.choice(['year', 'number', 'surname'])
        if suffix_type == 'year':
            return f"{name} {random.choice(range(1980, 2025))}"
        elif suffix_type == 'number':
            return f"{name} {random.choice(range(1, 100))}"
        else:  # surname
            surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
            return f"{name} {random.choice(surnames)}"
    return name

# Apply modification to the list of names
modified_names = [modify_name(name) for name in names]

dataset = []
for _ in range(len(modified_names)):
    name = random.choice(names)
    usernames = generate_usernames(name)
    dataset.append({"Given Name": name, "Potential Usernames": ", ".join(usernames)})


df=pd.DataFrame(dataset)
df.to_csv(r"C:\Users\Rajadurai\OneDrive\Documents\model dataset\username_dataset.csv",index=False)
print("datas inserted")