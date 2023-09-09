from django.contrib import admin

# Register your models here.

from .models import ( RoomMember,Users,Faculty_details,Subjects,Subject_handled,Test_evaluation,Details,Room,Message,class_enrolled,ClassRooms,Student,
Teacher,Course,Question,Result,blog,Draft_blog,Gallery,NoteCourse,Ebook,EbookForClass,URLForClass,Attendees,Sec_Daily_test_mark,
Internal_test_mark,Daily_test_mark,daily_test,Note,Event,Testimonials,logo,FooterEditPage,SocialMediaLinks,Pages,Department,YouTubeLink,
Category,Notifications,Assignment_mark,Assignment,Upload_Assignment,SocialMedia,BotControl,EmailSettings


)

admin.site.register(RoomMember)
admin.site.register(Users)
admin.site.register(Faculty_details)
admin.site.register(Subjects)
admin.site.register(Subject_handled)
admin.site.register(Test_evaluation)
admin.site.register(Details)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(class_enrolled)
admin.site.register(ClassRooms)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(blog)
admin.site.register(Draft_blog)
admin.site.register(Gallery)
admin.site.register(NoteCourse)
admin.site.register(Ebook)
admin.site.register(EbookForClass)
admin.site.register(URLForClass)
admin.site.register(Attendees)
admin.site.register(Sec_Daily_test_mark)
admin.site.register(Internal_test_mark)
admin.site.register(daily_test)
admin.site.register(Note)
admin.site.register(Event)
admin.site.register(Testimonials)
admin.site.register(logo)
admin.site.register(FooterEditPage)
admin.site.register(SocialMediaLinks)
admin.site.register(Pages)
admin.site.register(Department)
admin.site.register(YouTubeLink)
admin.site.register(Category)
admin.site.register(Notifications)
admin.site.register(Assignment)
admin.site.register(Assignment_mark)
admin.site.register(Upload_Assignment)
admin.site.register(SocialMedia)
admin.site.register(BotControl)
admin.site.register(EmailSettings)

