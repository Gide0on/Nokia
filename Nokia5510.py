print("""
##########---MENU FUNCTIONS---##########
1.Phone book
2.Messages
3.Chat
4.Call register
5.Tones
6.Setting
7.Call divert
8.Music
9.Games
10.Calculator
11.Reminders
12.Clock
13.Profiles
14.Services
15.SIM services
""")

mainmenu=int(input("Enter your choice : "))
match mainmenu:
	case 1:
		print(""""
		PHONE BOOK
		
		1. SERVICES
		2. SERVICE NOS
		3. ADD NAME
		4. ERASE
		5. EDIT
		6. COPY
		7. ASSIGN TONE
		8. SEND B'CARD
		9. OPTIONS
		10. SPEED DIALS
		11. VOICE TAGS
		""")
		
		phonebook=int(input("Enter your choice from 1 to 11: "))
		match phonebook:
			case 1:
				print("Services")
			case 2:
				print("Service Nos")
			case 3:
				print("Add name")
			case 4:
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Copy")
			case 7:
				print("Assign tone")
			case 8:
				print("Send b'card")
			case 9:
				print("Options")
				print("""
				1.MEMORY IN USE
				2.TYPE OF VIEW
				3.MEMORY STATUS
				""")
				options=int(input("Pick a number between 1 to 3: "))
				match options:
						case 1:
							print("Memory in use")
						case 2:
							print("Type of view")
						case 3:
							print("Memory status")
			case 10:
				print("Speed dials")
			case 11:
				print("Voice tags")

	case 2:
		print("""
		MESSAGES
		1. WRITE MESSAGES
		2. INBOX
		3. OUTBOX
		4. PICTURE MESSAGES
		5. TEMPLATES
		6. SMILEYS
		7. MESSAGE SETTINGS
		8. INFO SERVICE
		9. VOICE MAILBOX NUMBER
		10. SERVICE COMMAND EDITOR
		
		""")
		message_entry=int(input("Enter any number between 1 to 10: "))
		match message_entry:
			case 1:
				print("Write messages")
			case 2:
				print("Inbox")
			case 3:
				print("Outbox")
			case 4:
				print("Picture messages")
			case 5:
				print("Templates")
			case 6:
				print("Smileys")
			case 7:
				print("Message settings")
				print("""
				1.set 1
				2.Common
				""") 
				message_settings=int(input("Pick a number between 1 or 2: "))
				match message_settings:
					case 1:
						print("Set 1")
						print("""
						1.Message center number
						2.Message sent as
						3.Message validity
						""")
						
						set1=int(input("Pick a number between 1 to 3: "))
						match set1:
							case 1:
								print("Message center number")
							case 2:
								print("Message sent as")
							case 3:
								print("Message Validity")
					case 2:
						print("Common")
						print("""
						1.DELIVERY REPORTS
						2.REPLY VIA SAME CENTER
						3.CHARACTER SUPPORT
						""")

						
						common_entry=int(input("Pick a number between 1 to 3: "))
						match common_entry:
							case 1:
								print("Delivery reports")
							case 2:
								print("Reply via same centre")
							case 3:
								print("Character support")
			case 8:
				print("Info service")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editor")
	case 3:
		print("Chat")
	case 4:
		print("Call register")
		print("""
		1.MISSED CALLS
		2.RECEIVED CALLS
		3.DIALED NUMBERS
		4.ERASE RECENT CALL LISTS
		5.SHOW CALL DURATION
		""")
		callregister_entry=int(input("Enter any number between 1 to 8: "))
		match callregister_entry:
			case 1:
				print("Missed calls")
			case 2:
				print("Received calls")
			case 3:
				print("Dialed numbers")
			case 4:
				print("Erase recent call lists")
			case 5:
				print("Show call duration")
				print("""
				1.LAST CALL DURATION
				2.ALL CALLS' DURATION
				3.RECEIVED CALLS' DURATION
				4.DIALED CALLS' DURATION
				5.CLEAR TIMERS
				""")
				callduration_entry=int(input("Pick a number between 1 to 5: "))
				match callduration_entry:
					case 1:
						print("Last call duration")
					case 2:
						print("All calls' duration")
					case 3:
						print("Received calls' duration")
					case 4:
						print("Dialed calls' duration")
					case 5:
						print("Clear timers")


			case 6:
				print("Show call cost")
				print("""
				1.Last call cost
				2.All calls' duration
				3.Clear counters
				""")
				callcost_entry=int(input("Pick a number between 1 to 3: "))
				match callcost_entry:
					case 1:
						print("Last call cost")
					case 2:
						print("All calls' cost")
					case 3:
						print("Clear counters")
			case 7:
				print("Call cost settings")
				print("""
				1.CALL COST LIMIT
				2.SHOW COSTS IN
				""")
				costsetting_entry=int(input("Pick a number between 1 or 2: "))
				match costsetting_entry:
					case 1:
						print("Call cost limit")
					case 2:
						print("Show costs in")
			case 8:
				print("Prepaid credit")


	case 5:
		print("Tones")
		print("""
		1.RINGING TONE
		2.RINGING VOLUME
		3.INCOMING CALL ALERT
		4.MESSAGE ALERT TONE
		5.KEYPAD TONES
		6.WARNING TONES
		7.VIBRATING ALERT
		8.SCREEN SAVER
		""")
		tones=int(input("Enter a number between 1 to 8: "))
		match tones:
			case 1:
				print("Ringing tone")
			case 2:
				print("Ringing Volume")
			case 3:
				print("Incoming call alert")
			case 4:
				print("Message alert tone")
			case 5:
				print("Keypad tones")
			case 6:
				print("Warning tones")
			case 7:
				print("Vibrating alert")
			case 8:
				print("Screen saver")


		
	case 6:
		print("Settings")
		print("""
		1.CALL SETTINGS
		2.PHONE SETTINGS
		3.SECURITY SETTINGS
		4.RESTORE FACTORY SETTING
		""")
		setting=int(input("Pick a number between 1 and 4: "))
		match setting:
			case 1:
				print("Call settings")
				print("""
				1.AUTOMATIC REDIAL
				2.SPEED DIALING
				3.CALL WAITING OPTIONS
				4.OWN NUMBER SENDING
				5.PHONE LINE IN USE
				6.AUTOMATIC ANSWER
				""")
				callsetting_entry=int(input("Pick a number between 1 to 6: "))
				match callsetting_entry:
					case 1:
						print("Automatic redial")
					case 2:
						print("Speed dialing")
					case 3:
						print("Call waiting options")
					case 4:
						print("Own number sending")
					case 5:
						print("Phone line in use")
					case 6:
						print("Automatic answer")


			case 2:
				print("Phone settings")
				print("""
				1.LANGUAGE
				2.CELL INFO DISPLAY
				3.WELCOME NOTE
				4.NETWORK SELECTION
				5.CONFIRM SIM SERVICE ACTIONS
				""")
				phonesetting_entry=int(input("Pick a number between 1 to 5: "))
				match phonesetting_entry:
					case 1:
						print("Language")
					case 2:
						print("Cell info display")
					case 3:
						print("Welcome Note")
					case 4:
						print("Network selection")
					case 5:
						print("Confirm SIM service actions")

			case 3:
				print("Security settings")
				print("""
				1.PRINT CODE REQUEST
				2.CALL BARRING SERVICE
				3.FIXED DIALING
				4.CLOSED USER GROUP
				5.SECURITY LEVEL
				6.CHANGE ACCESS CODES
				""")

				securitysetting_entry=int(input("Pick a number between 1 to 6: "))
				match security_setting:
					case 1:
						print("PIN code request")
					case 2:
						print("Call barring service")
					case 3:
						print("Fixed dialing")
					case 4:
						print("Closed user group")
					case 5:
						print("Security level")
					case 6:
						print("Change access codes")

			case 4:
				print("Restore factory settings")

	case 7:
		print("Call divert")
	case 8:
		print("Music")
		print("""
		1.MUSIC PLAYER
		2.RADIO
		3.RECORDER
		4.TRACK LIST
		""")
		music=int(input("Pick a number between 1 to 4: "))
		match music:
			case 1:
				print("Music player")
			case 2:
				print("Radio")
			case 3:
				print("Recorder")
			case 4:
				print("Track list")

	case 9:
		print("Games")
	case 10:
		print("Calculator")
	case 11:
		print("Reminders")
	case 12:
		print("Clock")
		print("""
		1.ALARM CLOCK
		2.CLOCK SETTINGS
		3.DATE SETTING
		4.STOP WATCH
		5.COUNTDOWN TIMER
		6.AUTO UPDATE OF DATE AND TIME
		""")
		clock=int(input("Pick a number between 1 to 6: "))
		match clock:
			case 1:
				print("Alarm clock")
			case 2:
				print("Clock settings")
			case 3:
				print("Date setting")
			case 4:
				print("Stop watch")
			case 5:
				print("Countdown timer")
			case 6:
				print("Auto update of date and time")
	case 13:
		print("Profiles")
	case 14:
		print("Services")
	case 15:
		print("SIM services")

 
