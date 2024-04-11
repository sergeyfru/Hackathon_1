-- CREATE TABLE region(
-- 	region_id SERIAL PRIMARY KEY,
-- 	region_name VARCHAR (40) NOT NULL);

-- CREATE TABLE work_shift(
-- 	shift_id SERIAL PRIMARY KEY,
-- 	shift_name VARCHAR(25) NOT NULL);

-- CREATE TABLE work_day(
-- 	day_id SERIAL PRIMARY KEY,
-- 	day_name VARCHAR (20) NOT NULL);
	
-- CREATE TABLE frequency(
-- 	frequency_id SERIAL PRIMARY KEY,
-- 	frequency_rate VARCHAR (20) NOT NULL);

-- CREATE TABLE type_opp(
-- 	type_id SERIAL PRIMARY KEY,
-- 	type_name VARCHAR(40) NOT NULL);

-- CREATE TABLE subtype_opp(
-- 	subtype_id SERIAL PRIMARY KEY,
-- 	type_id INT REFERENCES type_opp(type_id),
-- 	subtype_name VARCHAR(100) NOT NULL);
	
-- CREATE TABLE volunteer(
-- 	volunteer_id SERIAL PRIMARY KEY,
-- 	v_first_name VARCHAR(50) NOT NULL,
-- 	v_last_name VARCHAR(50) NOT NULL,
-- 	v_email VARCHAR(50) UNIQUE,
-- 	v_phone INTEGER NOT NULL,
-- 	region_id INT REFERENCES region(region_id),
-- 	shift_id INT REFERENCES work_shift(shift_id),
-- 	day_id INT REFERENCES work_day(day_id),
-- 	frequency_id INT REFERENCES frequency(frequency_id),
-- 	type_id INT REFERENCES type_opp(type_id),
-- 	subtype_id INT REFERENCES subtype_opp(subtype_id));
	
-- CREATE TABLE opportunites(
-- 	opp_id SERIAL PRIMARY KEY,
-- 	opp_name VARCHAR(25) NOT NULL,
-- 	opp_email VARCHAR(25) UNIQUE,
-- 	opp_description VARCHAR(150),
-- 	region_id INT REFERENCES region(region_id),
-- 	shift_id INT REFERENCES work_shift(shift_id),
-- 	day_id INT REFERENCES work_day(day_id),
-- 	frequency_id INT REFERENCES frequency(frequency_id),
-- 	type_id INT REFERENCES type_opp(type_id),
-- 	subtype_id INT REFERENCES subtype_opp(subtype_id));





-- INSERT INTO region (region_name)
-- VALUES
--     ('Jerusalem'),
--     ('Tel Aviv'),
--     ('Haifa'),
--     ('Rishon LeZion'),
--     ('Petah Tikva'),
--     ('Ashdod'),
--     ('Netanya'),
--     ('Beer Sheva'),
--     ('Holon'),
--     ('Bnei Brak'),
--     ('Ramat Gan'),
--     ('Bat Yam'),
--     ('Ashkelon'),
--     ('Herzliya'),
--     ('Kfar Saba'),
--     ('Modiin-Maccabim-Reut'),
--     ('Hadera'),
--     ('Raanana'),
--     ('Lod'),
--     ('Nahariya'),
--     ('Ramat HaSharon'),
--     ('Rehovot'),
--     ('Nazareth'),
--     ('Givatayim'),
--     ('Kiryat Ata'),
--     ('Eilat'),
--     ('Acre'),
--     ('Bet Shemesh'),
--     ('Lakhish'),
--     ('Dimona'),
--     ('Arad'),
--     ('Afula'),
--     ('Tiberias'),
--     ('Beit Shemesh'),
--     ('Kiryat Yam'),
--     ('Nahal Oz'),
--     ('Kiryat Malakhi'),
--     ('Yavne'),
--     ('Safed'),
--     ('Yehud-Monosson'),
--     ('Maalot-Tarshiha'),
--     ('Nesher');

	
	
-- INSERT INTO work_shift (shift_name)
-- VALUES 
-- ('Morning Shift'),
-- ('Afternoon Shift'),
-- ('Evening Shift'),
-- ('Full-day');

-- INSERT INTO work_day (day_name) 
-- VALUES
-- ('Sunday'),('Monday'),('Tuesday'),('Wednesday'),('Thursday'),('Friday'),('Saturday');

-- INSERT INTO frequency (frequency_rate)
-- VALUES
-- ('1 X Week'),
-- ('2 X Week'),
-- ('3 X Week'),
-- ('4 X Week'),
-- ('5 X Week'),
-- ('6 X Week'),
-- ('More than two month');

-- INSERT INTO type_opp (type_name)
-- VALUES
--     ('Helping in shelters for homeless animals'),
--     ('Working in charity shops'),
--     ('Assisting in nursing homes'),
--     ('Environmental actions and projects'),
--     ('Teaching children and teenagers'),
--     ('Assisting in free clinics and hospitals'),
--     ('Organizing local events and festivals'),
--     ('Online volunteering'),
--     ('Aiding local homeless people'),
--     ('Helping people with disabilities');


-- INSERT INTO subtype_opp (subtype_name, type_id)
-- VALUES
--     ('Care for animals', 
-- 	(SELECT type_id FROM type_opp WHERE type_name = 'Helping in shelters for homeless animals')),
--     ('Walking dogs', 1),
--     ('Cleaning facilities', 1),
--     ('Assisting in adoption events', 1),
-- 	('Sorting and pricing items',
-- 	 (SELECT type_id FROM type_opp WHERE type_name = 'Working in charity shops')),
--     ('Assisting customers', 2),
--     ('Sales support', 2),
--     ('Maintaining cleanliness and order', 2),
-- 	('Socializing with elderly residents', (SELECT type_id FROM type_opp WHERE type_name = 'Assisting in nursing homes')),
--     ('Helping with daily tasks', 3),
--     ('Organizing recreational activities', 3),
--     ('Reading books and conversations', 3),

--     ('Cleaning up litter in parks and beaches', (SELECT type_id FROM type_opp WHERE type_name = 'Environmental actions and projects')),
--     ('Tree planting', 4),
--     ('Teaching local residents about ecology', 4),
--     ('Participating in environmental events', 4),

--     ('Assisting in schools and youth centers', (SELECT type_id FROM type_opp WHERE type_name = 'Teaching children and teenagers')),
--     ('Teaching specific subjects', 5),
--     ('Helping with homework', 5),
--     ('Organizing extracurricular activities', 5),

--     ('Assisting visitors', (SELECT type_id FROM type_opp WHERE type_name = 'Assisting in free clinics and hospitals')),
--     ('Supporting medical staff', 6),
--     ('Helping with documentation', 6),
--     ('Organizing events for patients', 6),

--     ('Assisting in organizing and hosting events', (SELECT type_id FROM type_opp WHERE type_name = 'Organizing local events and festivals')),
--     ('Support during the event day', 7),
--     ('Spreading information', 7),
--     ('Participating in organizing relaxation and entertainment areas', 7),

--     ('Translating texts for non-profit organizations', (SELECT type_id FROM type_opp WHERE type_name = 'Online volunteering')),
--     ('Assisting in web design', 8),
--     ('Managing social media', 8),
--     ('Online counseling and support', 8),

--     ('Distributing food and essential items', (SELECT type_id FROM type_opp WHERE type_name = 'Aiding local homeless people')),
--     ('Providing information on available services', 9),
--     ('Assisting in accessing medical help', 9),
--     ('Organizing events for social support', 9),

--     ('Assisting with daily tasks', (SELECT type_id FROM type_opp WHERE type_name = 'Helping people with disabilities')),
--     ('Accompanying to events', 10),
--     ('Assisting with transportation', 10),
--     ('Conducting individual sessions', 10);

-- INSERT INTO volunteer (v_first_name, v_last_name, v_email, v_phone, region_id, shift_id, day_id, frequency_id, type_id, subtype_id )
-- VALUES
-- ('John', 'Doe', 'john.doe@example.com', 0586449662,
-- 	 (SELECT region_id FROM region WHERE region_name = 'North'),
-- 	 (SELECT shift_id FROM work_shift WHERE shift_name = 'Morning Shift'),
-- 	 (SELECT day_id FROM work_day WHERE day_name = 'Monday'),
-- 	 (SELECT frequency_id FROM frequency WHERE frequency_rate = 'All days'),
-- 	 (SELECT type_id FROM type_opp WHERE type_name = 'Assisting in free clinics and hospitals'),
-- 	 (SELECT subtype_id FROM subtype_opp WHERE subtype_name = 'Supporting medical staff')),
	 
-- ('Jane', 'Smith', 'janesmith@example.com', '0529876543', 2, 2, 2, 2, 2, 2),
-- ('David', 'Cohen', 'davidcohen@example.com', '0543210987', 3, 3, 3, 3, 3, 3),
-- ('Sarah', 'Levy', 'sarahlevy@example.com', '0587654321', 4, 4, 4, 4, 4, 4),
-- ('Michael', 'Goldberg', 'michaelgoldberg@example.com', '0532468109', 5, 1, 5, 5, 5, 5),
-- ('Rachel', 'Rosenberg', 'rachelrosenberg@example.com', '0556789012', 6, 2, 6, 6, 6, 6),
-- ('Daniel', 'Levi', 'daniellevi@example.com', '0567890123', 7, 3, 7, 1, 7, 7),
-- ('Rebecca', 'Davidson', 'rebeccadavidson@example.com', '0578901234', 8, 4, 1, 2, 8, 8),
-- ('Ethan', 'Cohen', 'ethancohen@example.com', '0512345678', 9, 1, 2, 3, 9, 9),
-- ('Olivia', 'Friedman', 'oliviafriedman@example.com', '0598765432', 10, 2, 3, 4, 10, 10),
-- ('Liam', 'Shapiro', 'liamshapiro@example.com', '0501112223', 11, 3, 4, 5, 1, 11),
-- ('Emma', 'Cohen', 'emmacohen@example.com', '0523334445', 12, 4, 5, 6, 2, 12),
-- ('Noah', 'Levy', 'noahlevy@example.com', '0545556667', 13, 1, 6, 7, 3, 13),
-- ('Ava', 'Goldstein', 'avagoldstein@example.com', '0567778889', 14, 2, 7, 1, 4, 14),
-- ('William', 'Rosen', 'williamrosen@example.com', '0589990001', 15, 3, 1, 2, 5, 15),
-- ('Sophia', 'Katz', 'sophiakatz@example.com', '0511121314', 16, 4, 2, 3, 6, 16),
-- ('James', 'Weiss', 'jamesweiss@example.com', '0533343536', 17, 1, 3, 4, 7, 17),
-- ('Isabella', 'Feldman', 'isabellafeldman@example.com', '0555565758', 18, 2, 4, 5, 8, 18),
-- ('Benjamin', 'Gershon', 'benjamingershon@example.com', '0577788990', 19, 3, 5, 6, 9, 19),
-- ('Mia', 'Shmueli', 'miashmueli@example.com', '0599900012', 20, 4, 6, 7, 10, 20),
-- ('Ella', 'Cohen', 'ellacohen@example.com', '0501122334', 21, 1, 1, 1, 1, 21),
-- ('Jacob', 'Levine', 'jacoblevine@example.com', '0523344556', 22, 2, 2, 2, 2, 22),
-- ('Arielle', 'Rabinovich', 'ariellerabinovich@example.com', '0545566778', 23, 3, 3, 3, 3, 23),
-- ('Max', 'Weiss', 'maxweiss@example.com', '0567788990', 24, 4, 4, 4, 4, 24),
-- ('Sophie', 'Goldberg', 'sophiegoldberg@example.com', '0589900012', 25, 1, 5, 5, 5, 25),
-- ('Zachary', 'Feldman', 'zacharyfeldman@example.com', '0512233445', 26, 2, 6, 6, 6, 26),
-- ('Leah', 'Katz', 'leahkatz@example.com', '0534455667', 27, 3, 7, 1, 7, 27),
-- ('Daniel', 'Cohen', 'danielcohen@example.com', '0556677889', 28, 4, 1, 2, 8, 28),
-- ('Hannah', 'Grossman', 'hannahgrossman@example.com', '0577899001', 29, 1, 2, 3, 9, 29),
-- ('Ethan', 'Stein', 'ethanstein@example.com', '0590011223', 30, 2, 3, 4, 10, 30),
-- ('Ava', 'Rosenbaum', 'avarosenbaum@example.com', '0502345678', 31, 3, 4, 5, 1, 31),
-- ('Noah', 'Levi', 'noahlevi@example.com', '0524567890', 32, 4, 5, 6, 2, 32),
-- ('Emma', 'Eisenberg', 'emmaeisenberg@example.com', '0546789012', 33, 1, 6, 7, 3, 33),
-- ('Liam', 'Cohen', 'liamcohen@example.com', '0567890123', 34, 2, 7, 1, 4, 34),
-- ('Olivia', 'Avraham', 'oliviaavraham@example.com', '0589012345', 35, 3, 1, 2, 5, 35),
-- ('Benjamin', 'Leibowitz', 'benjaminleibowitz@example.com', '0511123456', 36, 4, 2, 3, 6, 36),
-- ('Sophia', 'Berkowitz', 'sophiaberkowitz@example.com', '0533345678', 37, 1, 3, 4, 7, 37),
-- ('William', 'Weiss', 'williamweiss@example.com', '0555567890', 38, 2, 4, 5, 8, 38),
-- ('Emily', 'Cohen', 'emilycohen@example.com', '0577789012', 39, 3, 5, 6, 9, 39),
-- ('Alexander', 'Friedman', 'alexanderfriedman@example.com', '0599901234', 40, 4, 6, 7, 10, 40);

-- INSERT INTO opportunites (opp_name, opp_email,opp_description, region_id, shift_id, day_id, frequency_id, type_id, subtype_id )
-- VALUES

-- ('Animal Shelter Volunteer', 'animalshelter@example.com','Help care for animals in need of homes',
--  (SELECT region_id FROM region WHERE region_name = 'North'),
--  (SELECT shift_id FROM work_shift WHERE shift_name = 'Morning Shift'),
--  (SELECT day_id FROM work_day WHERE day_name = 'Monday'),
--  (SELECT frequency_id FROM frequency WHERE frequency_rate = 'All days'),
--  (SELECT type_id FROM type_opp WHERE type_name = 'Assisting in free clinics and hospitals'),
--  (SELECT subtype_id FROM subtype_opp WHERE subtype_name = 'Supporting medical staff')),

-- ('Charity Shop Assistant', 'charityshop@example.com', 'Help with sorting and selling donated items.', 2, 2, 2, 2, 2, 2),
--     ('Elderly Care Companion', 'elderlycare@example.com', 'Provide companionship and assistance to elderly residents.', 3, 3, 3, 3, 3, 3),
--     ('Beach Cleanup Crew', 'beachcleanup@example.com', 'Join efforts to clean up litter on local beaches.', 4, 4, 4, 4, 4, 4),
--     ('After-School Tutor', 'tutoring@example.com', 'Assist students with homework and educational activities.', 5, 1, 5, 5, 5, 5),
--     ('Hospital Volunteer', 'hospitalvolunteer@example.com', 'Support hospital staff and assist patients.', 6, 2, 6, 6, 6, 6),
--     ('Local Festival Organizer', 'festivalorganizer@example.com', 'Help plan and execute community festivals.', 7, 3, 7, 7, 7, 7),
--     ('Online Translator', 'translator@example.com', 'Translate texts for non-profit organizations.', 8, 4, 1, 2, 8, 8),
--     ('Homeless Outreach Volunteer', 'homelessoutreach@example.com', 'Provide food and resources to homeless individuals.', 9, 1, 2, 4, 9, 9),
--     ('Disability Support Assistant', 'disabilitysupport@example.com', 'Assist individuals with disabilities in daily tasks.', 10, 2, 3, 1, 10, 10),
-- 	('Dog Walking Volunteer', 'dogwalking@example.com', 'Take shelter dogs on walks to help them stay healthy and socialized.', 1, 2, 3, 1, 2, 11),
--     ('Clothing Drive Organizer', 'clothingdrive@example.com', 'Coordinate and promote clothing donation drives for those in need.', 2, 3, 4, 2, 3, 12),
--     ('Memory Care Assistant', 'memorycare@example.com', 'Help individuals with memory impairments engage in activities and socialization.', 3, 4, 5, 3, 4, 13),
--     ('Park Conservation Volunteer', 'parkconservation@example.com', 'Assist in preserving local parks through cleanup and maintenance efforts.', 4, 1, 6, 4, 5, 14),
--     ('Youth Mentor', 'youthmentor@example.com', 'Guide and mentor young people in developing positive life skills and goals.', 5, 2, 7, 5, 6, 15),
--     ('Medical Records Clerk', 'recordsclerk@example.com', 'Help organize and maintain patient records in a healthcare setting.', 6, 3, 1, 6, 7, 16),
--     ('Cultural Event Coordinator', 'culturalevent@example.com', 'Assist in organizing cultural events that celebrate diversity and inclusivity.', 7, 4, 2, 7, 8, 17),
--     ('Social Media Manager', 'socialmedia@example.com', 'Manage social media accounts to promote non-profit initiatives and events.', 8, 1, 3, 3, 9, 18),
--     ('Soup Kitchen Volunteer', 'soupkitchen@example.com', 'Serve meals and provide support to those experiencing food insecurity.', 9, 2, 4, 2, 10, 19),
--     ('Adaptive Sports Assistant', 'adaptivesports@example.com', 'Assist athletes with disabilities in adaptive sports programs.', 10, 3, 5, 1, 10, 20),
--     ('Veterinary Clinic Volunteer', 'vetclinic@example.com', 'Assist veterinary staff with animal care and clinic operations.', 1, 4, 6, 1, 3, 21),
--     ('Bookstore Clerk', 'bookstore@example.com', 'Help organize and sell books in a bookstore supporting literacy programs.', 2, 1, 7, 2, 4, 22),
--     ('Dementia Support Group Facilitator', 'dementiasupport@example.com', 'Lead support group sessions for individuals with dementia and their families.', 3, 2, 1, 3, 5, 23),
--     ('Trail Maintenance Crew', 'trailmaintenance@example.com', 'Maintain hiking trails and natural areas for public enjoyment.', 4, 3, 2, 4, 6, 24),
--     ('Art Workshop Instructor', 'artworkshop@example.com', 'Teach art classes to children and adults in community art programs.', 5, 4, 3, 5, 7, 25),
--     ('Emergency Room Assistant', 'emergencyroom@example.com', 'Assist in the emergency room with patient intake and support.', 6, 1, 4, 6, 8, 26),
--     ('Street Fair Volunteer', 'streetfair@example.com', 'Help set up and manage booths at local street fairs and markets.', 7, 2, 5, 7, 9, 27),
--     ('Grant Writer', 'grantwriter@example.com', 'Research and write grant proposals for non-profit funding opportunities.', 8, 3, 6, 6, 10, 28),
--     ('Shelter Meal Prep Volunteer', 'mealprep@example.com', 'Prepare and serve meals at homeless shelters and soup kitchens.', 18, 2, 4, 6, 10, 29);



