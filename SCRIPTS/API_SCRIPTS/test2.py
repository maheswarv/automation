a = {"sendMail": false,
     "jsonFilter": {"isApplicantDataRestrictedByFilters": false, "testFilter": {}, "interviewFilter": {},
                    "jobIds": [28135]}, "templateJSON": {"format_rules": {
        "header_format": {"bold": 1, "border": 1, "border_color": "#000000", "align": "center", "valign": "vcenter",
                          "color": "#ffffff", "fg_color": "#006fa6"},
        "missing_info_format": {"align": "center", "valign": "vcenter"},
        "align_center": {"align": "center", "valign": "vcenter"},
        "string_format": {"align": "center", "valign": "vcenter", "num_format": "@"},
        "date": {"align": "center", "valign": "vcenter", "num_format": "DD MMM YYYY"},
        "dateTime": {"align": "center", "valign": "vcenter", "num_format": "HH:mm:ss DD MMM YYYY"},
        "wrap_text": {"align": "center", "valign": "vcenter", "text_wrap": true},
        "group_column_format": {"align": "center", "valign": "vcenter", "bg_color": "#FFFF00", "fg_color": "#000000",
                                "pattern": 1, "border": 1, "border_color": "#000000"},
        "task_details_first_column": {"align": "center", "valign": "vcenter", "bg_color": "#87ceeb",
                                      "fg_color": "#000000", "pattern": 1, "border": 1, "border_color": "#000000"},
        "interview_column_format": {"align": "center", "valign": "vcenter", "bg_color": "#87ceeb",
                                    "fg_color": "#000000", "pattern": 1, "border": 1, "border_color": "#000000"},
        "num_format": {"num_format": "0.00", "align": "center", "valign": "vcenter"}}, "file_meta_rules": {
        "file_name": "11035371-5641-4793-b95d-7589e31a_28135AiReportJob1To12"},
                                                         "transform_rules": ["SPLIT_ED_PROFILE", "CANDIDATE_BASIC",
                                                                             "APPLICANT_OWNERS", "FORM_CONTENT",
                                                                             "TEST_DETAILS", "TASK_INFORMATION",
                                                                             "REMOVE_UNWANTED_KEYS",
                                                                             "APP_ENTITY_COMMUNICATION",
                                                                             "REMOVE_KEYS_WITH_NULL",
                                                                             "REMOVE_KEYS_WITH_EMPTY_VALUE",
                                                                             "NEW_INTERVIEW_FEEDBACK"],
                                                         "transform_options": {"REMOVE_UNWANTED_KEYS": {
                                                             "keys_to_remove": ["interviewDetails",
                                                                                "BLUEPRINT_TEST_DETAILS",
                                                                                "filledFormDetails", "activityDetails",
                                                                                "offerDetails", "communicationDetails",
                                                                                "taskDetails", "testDetails",
                                                                                "SPLIT_ED_PROFILE", "CANDIDATE_BASIC",
                                                                                "APPLICANT_OWNERS", "FORM_CONTENT",
                                                                                "TEST_DETAILS", "TASK_SUMMARY",
                                                                                "TASK_INFORMATION"]}},
                                                         "content_rules": [
                                                             {"columnName": "Applicant Id", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["applicantDetail", "applicantId"],
                                                              "default": " ", "id": "ApplicantId"},
                                                             {"columnName": "Event Id", "format": "align_center",
                                                              "accessor": ["eventDetails", "eventId"], "default": " ",
                                                              "id": "EventId"},
                                                             {"columnName": "Event Name", "format": "align_center",
                                                              "accessor": ["eventDetails", "eventName"], "default": " ",
                                                              "id": "EventName"},
                                                             {"columnName": "Candidate Id", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "candidateId"],
                                                              "default": " ", "id": "CandidateId"},
                                                             {"columnName": "Candidate Name", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "fullName"],
                                                              "default": " ", "id": "Name"},
                                                             {"columnName": "First Name", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "firstName"],
                                                              "default": " ", "id": "FirstName"},
                                                             {"columnName": "Middle Name", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "middleName"],
                                                              "default": " ", "id": "MiddleName"},
                                                             {"columnName": "Last Name", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "lastName"],
                                                              "default": " ", "id": "LastName"},
                                                             {"columnName": "Primary Email", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "primaryEmail"],
                                                              "default": " ", "id": "Email1"},
                                                             {"columnName": "Mobile", "format": "string_format",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "mobile"],
                                                              "default": " ", "id": "Mobile1"},
                                                             {"columnName": "USN", "format": "string_format",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "usn"], "default": " ",
                                                              "id": "Usn"},
                                                             {"columnName": "Business Unit", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["masterJobRequisitionDetails",
                                                                           "taggedJobBu"], "default": " ",
                                                              "id": "JobDepartment"},
                                                             {"columnName": "Job Location", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["masterJobRequisitionDetails",
                                                                           "taggedJobLocation"], "default": " ",
                                                              "id": "JobLocation"},
                                                             {"columnName": "Current Status", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["applicantDetail", "currentStatusLabel"],
                                                              "default": " ", "id": "CurrentStatus"},
                                                             {"columnName": "Current Stage", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["applicantDetail", "currentStageLabel"],
                                                              "default": " ", "id": "CurrentStage"},
                                                             {"columnName": "Father Name", "format": "align_center",
                                                              "accessor": ["candidateDetails", "familyDetails",
                                                                           "fatherName"], "default": " ",
                                                              "id": "FamilyDetails"},
                                                             {"columnName": "Mother Name", "format": "align_center",
                                                              "accessor": ["candidateDetails", "familyDetails",
                                                                           "motherName"], "default": " ",
                                                              "id": "FamilyDetails"}, {"columnName": "No Of Dependents",
                                                                                       "format": "align_center",
                                                                                       "accessor": ["candidateDetails",
                                                                                                    "familyDetails",
                                                                                                    "familyDependents"],
                                                                                       "default": " ",
                                                                                       "id": "FamilyDetails"},
                                                             {"columnName": "Family Income", "format": "align_center",
                                                              "accessor": ["candidateDetails", "familyDetails",
                                                                           "totalHouseIncomeInLakhs"], "default": " ",
                                                              "id": "FamilyDetails"},
                                                             {"columnName": "Annual Income", "format": "align_center",
                                                              "accessor": ["candidateDetails", "familyDetails",
                                                                           "annualIncomeInLakhs"], "default": " ",
                                                              "id": "FamilyDetails"},
                                                             {"columnName": "No Of Sibilings", "format": "align_center",
                                                              "accessor": ["candidateDetails", "familyDetails",
                                                                           "familySiblings"], "default": " ",
                                                              "id": "FamilyDetails"},
                                                             {"columnName": "Source", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "CANDIDATE_BASIC",
                                                                           "originalSource"], "default": " ",
                                                              "id": "OriginalSource"},
                                                             {"columnName": "Hierarchy", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "hierarchy"],
                                                              "default": " ", "id": "Hierarchy"},
                                                             {"columnName": "Current CTC", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "currentCTC"],
                                                              "default": " ", "id": "CurrentCTC"},
                                                             {"columnName": "Secondary Expertise",
                                                              "format": "align_center", "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "expertise2"],
                                                              "default": " ", "id": "Expertise2"},
                                                             {"columnName": "Primary Expertise",
                                                              "format": "align_center", "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "expertise1"],
                                                              "default": " ", "id": "Expertise1"},
                                                             {"columnName": "Current Location",
                                                              "format": "align_center", "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "currentLocation"],
                                                              "default": " ", "id": "CurrentLocation"},
                                                             {"columnName": "Sensitivity", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "sensitivity"],
                                                              "default": " ", "id": "Sensitivity"},
                                                             {"columnName": "Country", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "country"],
                                                              "default": " ", "id": "Country"},
                                                             {"columnName": "Nationality", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "nationality"],
                                                              "default": " ", "id": "Nationality"},
                                                             {"columnName": "Passport Number", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "passportNumber"],
                                                              "default": " ", "id": "Passport"},
                                                             {"columnName": "Pancard Number", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "panNumber"],
                                                              "default": " ", "id": "Pancard"},
                                                             {"columnName": "Primary Address", "format": "wrap_text",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "primaryAddress"],
                                                              "default": " ", "id": "Address1"},
                                                             {"columnName": "Secondary Address", "format": "wrap_text",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "secondaryAddress"],
                                                              "default": " ", "id": "Address2"},
                                                             {"columnName": "Other Address", "format": "wrap_text",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "alternativeAddress"],
                                                              "default": " ", "id": "Address3"},
                                                             {"columnName": "Secondary Phone",
                                                              "format": "string_format", "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "phoneResidence"],
                                                              "default": " ", "id": "PhoneResidence"},
                                                             {"columnName": "Phone Office", "format": "string_format",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "phoneOffice"],
                                                              "default": " ", "id": "PhoneOffice"},
                                                             {"columnName": "Marital Status", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "maritalStatus"],
                                                              "default": " ", "id": "MaritalStatus"},
                                                             {"columnName": "Gender", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "gender"],
                                                              "default": " ", "id": "Gender"},
                                                             {"columnName": "Date Of Birth", "format": "date",
                                                              "is_date": true, "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "dateOfBirth"],
                                                              "default": " ", "id": "DateOfBirth"},
                                                             {"columnName": "Secondary Email", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "alternateEmail"],
                                                              "default": " ", "id": "Email2"},
                                                             {"columnName": "Job Id", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["jobDetails", "jobId"], "default": " ",
                                                              "id": "JobId"},
                                                             {"columnName": "Job Name", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["jobDetails", "jobName"], "default": " ",
                                                              "id": "JobName"},
                                                             {"columnName": "Work Profiles", "format": "align_center",
                                                              "include_child_indexed_header": "True",
                                                              "include_child_enveloping_header": "True",
                                                              "accessor": ["candidateDetails", "workProfiles"],
                                                              "next": [{"columnName": "Designation Name",
                                                                        "format": "align_center",
                                                                        "accessor": "designation", "default": " ",
                                                                        "id": "DesignationName"},
                                                                       {"columnName": "Company Name",
                                                                        "format": "align_center",
                                                                        "force_inclusion": "True",
                                                                        "accessor": "employer", "default": " ",
                                                                        "id": "CompanyName"},
                                                                       {"columnName": "Location Name",
                                                                        "format": "align_center",
                                                                        "accessor": "locationText", "default": " ",
                                                                        "id": "LocationName"},
                                                                       {"columnName": "Yearly Salary",
                                                                        "format": "align_center",
                                                                        "accessor": "yearlySalaryInLakhs",
                                                                        "default": " ", "id": "YearlySalary"},
                                                                       {"columnName": "Reason For Leaving",
                                                                        "format": "align_center",
                                                                        "accessor": "reasonForLeaving", "default": " ",
                                                                        "id": "ReasonForLeaving"},
                                                                       {"columnName": "Worked From Month",
                                                                        "format": "align_center",
                                                                        "force_inclusion": "True",
                                                                        "accessor": "fromMonth", "default": " ",
                                                                        "id": "WorkedFromMonth"},
                                                                       {"columnName": "Worked From Year",
                                                                        "format": "align_center",
                                                                        "force_inclusion": "True",
                                                                        "accessor": "fromYear", "default": " ",
                                                                        "id": "WorkedFromYear"},
                                                                       {"columnName": "Worked To Month",
                                                                        "format": "align_center",
                                                                        "force_inclusion": "True",
                                                                        "accessor": "toMonth", "default": " ",
                                                                        "id": "WorkedToMonth"},
                                                                       {"columnName": "Worked To Year",
                                                                        "format": "align_center",
                                                                        "force_inclusion": "True", "accessor": "toYear",
                                                                        "default": " ", "id": "WorkedToYear"},
                                                                       {"columnName": "Title", "format": "align_center",
                                                                        "accessor": "title", "default": " ",
                                                                        "id": "Title"}, {"columnName": "Experience",
                                                                                         "format": "align_center",
                                                                                         "accessor": "experienceInMonths",
                                                                                         "default": " ",
                                                                                         "id": "Experience"},
                                                                       {"columnName": "Expertise",
                                                                        "format": "align_center",
                                                                        "accessor": "expertise", "default": " ",
                                                                        "id": "Expertise"},
                                                                       {"columnName": "Sub Expertise",
                                                                        "format": "align_center",
                                                                        "accessor": "subExpertise", "default": " ",
                                                                        "id": "SubExpertise"},
                                                                       {"columnName": "Sub Expertise2",
                                                                        "format": "align_center",
                                                                        "accessor": "subExpertise2", "default": " ",
                                                                        "id": "SubExpertise2"},
                                                                       {"columnName": "Industry",
                                                                        "format": "align_center",
                                                                        "accessor": "industry", "default": " ",
                                                                        "id": "Industry"}, {"columnName": "Latest",
                                                                                            "format": "align_center",
                                                                                            "force_inclusion": "True",
                                                                                            "override_column_length": 9,
                                                                                            "aliases": {"0": "No",
                                                                                                        "1": "Yes"},
                                                                                            "accessor": "isLatest",
                                                                                            "default": " ",
                                                                                            "id": "IsLatest"}],
                                                              "default": " ", "id": "CandidateWorkProfiles"},
                                                             {"columnName": "Skills", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "technologyText"],
                                                              "default": " ", "id": "TechnologyText"},
                                                             {"columnName": "BPO Experience", "format": "align_center",
                                                              "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "CANDIDATE_BASIC",
                                                                           "bpoExperience"], "default": " ",
                                                              "id": "BpoExperience"},
                                                             {"columnName": "Current Experience",
                                                              "format": "align_center", "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "CANDIDATE_BASIC",
                                                                           "currentExperience"], "default": " ",
                                                              "id": "CurrentExperience"},
                                                             {"columnName": "Total Experience",
                                                              "format": "align_center", "force_inclusion": "True",
                                                              "accessor": ["candidateDetails", "CANDIDATE_BASIC",
                                                                           "totalExperience"], "default": " ",
                                                              "id": "TotalExperience"}]},
     "jsonOptions": {"candidateDetails": {"isRequired": true, "socialNetworkRequired": false},
                     "testDetails": {"isRequired": false, "testLinkRequired": false,
                                     "isTypingQuestionDetailsRequired": false, "isTestUserLoginInfoRequired": false,
                                     "isSectionQuestionDetailsRequired": false,
                                     "isAudioTranscriptDetailsRequired": false},
                     "interviewDetails": {"isRequired": false, "isShortenUrlRequired": false,
                                          "isEntityCommunicationDetailsRequired": false},
                     "pofuDetails": {"isRequired": false}, "attachmentDetails": {"isRequired": false},
                     "jobDetails": {"isRequired": true},
                     "applicantDetails": {"applicantHistoryDetails": {"isRequired": false},
                                          "isAssessmentSlotInfoRequired": true}, "offerDetails": {"isRequired": false},
                     "eventDetails": {"isRequired": true}, "masterJobRequisitionDetails": {"isRequired": true},
                     "jobPositionDetails": {"isRequired": false}, "communicationDetails": {"isRequired": false},
                     "rpoDetails": {"isRequired": false}, "paymentDetails": {}}, "invokeSync": false, "reportType": 0}
