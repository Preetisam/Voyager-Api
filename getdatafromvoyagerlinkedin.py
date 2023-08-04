def getdatafromvoyagerlinkedin(company_id):
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
               }

    company_link = f'https://www.linkedin.com/voyager/api/entities/companies/{company_id}'

    with requests.session() as s:
        s.cookies['li_at'] = "AQEDATf5D_XXXXXXXXXXXXXXu"
        s.cookies["JSESSIONID"] = "ajax:1XXXXXXXXXXXXXX0"
        s.headers = headers
        s.headers["csrf-token"] = s.cookies["JSESSIONID"].strip('"')
        response = s.get(company_link)
        response_dict = response.json()
        return response_dict


print(getdatafromvoyagerlinkedin(16198870))
# Output
#{'employeeCountRange': '11-50',
 #'specialties': ['Web Development', 
#'Mobile App Development', 'Web Design', 
#'Node', 'Flutter', 'Ionic', 'AWS', 'Digital Ocean', 'Laravel', 'WordPress', 
#'React Native', 'React JS experts', 'PHP development', 'PrestaShop', 'OpenCart',
# 'SEO and SEM', 'Joomla'],
 #'entityUrn': 'urn:li:fs_company:16198870', 
#'websiteUrl': 'https://www.bytescrum.com', 
#'companyType': 'Privately Held', 'foundedDate': {'year': 2017}, 
#'entityInfo': {'objectUrn': 'urn:li:company:16198870',
#'trackingId': 'ymxYkL2eSUSOWQIt+Mn3xQ=='}, 
#'industries': ['Information Technology and Services'],
 #'description': 'ByteScrum taps into its strong business acumen to find solutions to the unique set of challenges and constraints imposed by each new project and delivers solutions that fill performance gaps. 
#Our founders understood for the first time how good software development services can transform the needs of entire business communities, especially emerging technologies.
# We have a proven track record of successfully meeting deadlines and executing the most complex projects within budget while consistently maintaining the highest quality.\n\nOur specialities:\n\n● Mobile app development
 #(Android and iOS)\n● Web app development (MERN, MEAN, Vue JS, PHP, Laravel, WordPress)\n● Custom Software development\n● Web designing (PSD to HTML/WordPress)\n● Api integration \n● 
#CMS development\n● Web and app service integration\n● SEO and SEM services\n\nContact Us:\nhttps://www.bytescrum.com/contact-us/', 
#'basicCompanyInfo': {'headquarters': 'Lucknow',
 #'followingInfo': {'entityUrn': 'urn:li:fs_followingInfo:urn:li:company:16198870', 
#'dashFollowingStateUrn': 'urn:li:fsd_followingState:urn:li:fsd_company:16198870', 'following': False, 'trackingUrn': 'urn:li:company:16198870', 'followingType': 'DEFAULT'},
# 'miniCompany': {'objectUrn': 'urn:li:company:16198870', 'entityUrn': 'urn:li:fs_miniCompany:16198870', 'name': 'ByteScrum Technologies Private Limited',
# 'showcase': False, 
#'active': True,
# 'logo': {'com.linkedin.common.VectorImage': {'artifacts': [{'width': 200, 'fileIdentifyingUrlPathSegment': '200_200/0/1653201669588?e=1698883200&v=beta&t=GE_5HHCt3u_xxKWDV1d3KmNBx0-AJXvIyjkIxSaXp-E',
# 'expiresAt': 1698883200000, 'height': 200}, {'width': 100, 'fileIdentifyingUrlPathSegment': '100_100/0/1653201669588?e=1698883200&v=beta&t=rbIH_vzfS4YkrOV-inNhuY9XXdbj28K9l4ZY_4-I41o', 
#'expiresAt': 1698883200000, 'height': 100}, {'width': 400, 'fileIdentifyingUrlPathSegment':
# '400_400/0/1653201669588?e=1698883200&v=beta&t=rARzTyswXT1D9vObNkCAh9ljFivi4r6T0QxC_WwLVvQ', 'expiresAt': 1698883200000, 'height': 400}], 
#'rootUrl': 'https://media.licdn.com/dms/image/C4D0BAQHzTgUzh6WpUw/company-logo_'}}, 'universalName': 'bytescrum', 'dashCompanyUrn': 'urn:li:fsd_company:16198870', 
#'trackingId': 'XXXXXXXXXXXXXXXXX'}}}
