create table video (
	id integer auto_increment not null,
	type varchar(30) not null default 'internal',
	video_id varchar(255) null,
	video_title varchar(200) null,
	video_description longtext null,
	video_author varchar(100) null,
	video_url varchar(255) not null,
	title varchar(200) null,
	description longtext null,
	alias varchar(255) not null,
	thumb varchar(255) null,
	created_at datetime not null,
	updated_at datetime not null,
	primary key (id)
) engine=InnoDB default charset=utf8 collate=utf8_unicode_ci auto_increment=1;

create table course(
	id integer auto_increment not null,
	title varchar(200) null,
	description longtext null,
	alias varchar(255) not null,
	author varchar(100) null,
	tags longtext null,
	created_at datetime not null,
	updated_at datetime not null,
	primary key (id)
) engine=InnoDB default charset=utf8 collate=utf8_unicode_ci auto_increment=1;

create table course_video(
	id integer auto_increment not null,
	course_id integer not null,
	video_id integer not null,
	video_order integer not null,
	video_title varchar(100) null,
	created_at datetime not null,
	updated_at datetime not null,
	primary key (id)
) engine=InnoDB default charset=utf8 collate=utf8_unicode_ci auto_increment=1;

insert into video(type, video_id, video_title, video_description, video_author, video_url, title, alias, created_at, updated_at) 
	values
		('youtube', 'yRzsOOiJ_p4', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=yRzsOOiJ_p4', '', '', curdate(), curdate()),
		('youtube', 'ntL8QDOhhL8', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=ntL8QDOhhL8', '', '', curdate(), curdate()),
		('youtube', 'oTBcGPXH6K0', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=oTBcGPXH6K0', '', '', curdate(), curdate()),
		('youtube', 'LKGGWsXyiyo', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=LKGGWsXyiyo', '', '', curdate(), curdate()),
		('youtube', '-wDAPo9hpCg', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=-wDAPo9hpCg', '', '', curdate(), curdate()),
		('youtube', 'fAXETAyrv8s', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=fAXETAyrv8s', '', '', curdate(), curdate()),
		('youtube', 'bMGXYEg1gJo', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=bMGXYEg1gJo', '', '', curdate(), curdate()),
		('youtube', 'VGs_lMw2hQg', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=VGs_lMw2hQg', '', '', curdate(), curdate()),
		('youtube', '_GZmuvmgtUc', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=_GZmuvmgtUc', '', '', curdate(), curdate()),
		('youtube', 'Oz4KYZ9KLc0', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=Oz4KYZ9KLc0', '', '', curdate(), curdate()),
		('youtube', 'nB_bVJ1c1Rg', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=nB_bVJ1c1Rg', '', '', curdate(), curdate()),
		('youtube', 'ZVTbRNu2BI0', '', '', 'Eli Fieldsteel', 'http://www.youtube.com/watch?v=ZVTbRNu2BI0', '', '', curdate(), curdate());

insert into course(title, description, alias, tags, author, created_at, updated_at) 
	values ('SuperCollider Tutorial', 'SuperCollider was developed by James McCartney and originally released in 1996. He released it under the terms of the GNU General Public License in 2002 when he joined the Apple Core Audio team. It is now maintained and developed by an active and enthusiastic community. It is used by musicians, scientists, and artists working with sound.', 'supercollider-tutorial', 'supercollider, programming basics, audio' , 'Eli Fieldsteel', curdate(), curdate());


insert into course_video(course_id, video_id, video_order, video_title, created_at, updated_at)
	values
		(1, 1, 1, 'Chapter 1', curdate(), curdate()),
		(1, 2, 2, 'Chapter 2', curdate(), curdate()),
		(1, 3, 3, 'Chapter 3', curdate(), curdate()),
		(1, 4, 4, 'Chapter 4', curdate(), curdate()),
		(1, 5, 5, 'Chapter 5', curdate(), curdate()),
		(1, 6, 6, 'Chapter 6', curdate(), curdate()),
		(1, 7, 7, 'Chapter 7', curdate(), curdate()),
		(1, 8, 8, 'Chapter 8', curdate(), curdate()),
		(1, 9, 9, 'Chapter 9', curdate(), curdate()),
		(1, 10, 10, 'Chapter 10', curdate(), curdate()),
		(1, 11, 11, 'Chapter 11', curdate(), curdate()),
		(1, 12, 12, 'Chapter 12', curdate(), curdate());

select * from course as c join course_video as cv on c.id = cv.course_id join video as v on v.id = cv.video_id;