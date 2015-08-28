puts "Hello and welcome to Roman Menzel's GuessMyNumberGame :)"
difficulty = {'easy' => rand(10), 'medium' => rand(100), 'hard' => rand(1000), 'very hard' => rand(10000)}
tries = 0

puts "Selcect a difficulty"
puts "1.) Easy"
puts "2.) Medium"
puts "3.) Hard"
puts "4.) Very hard"
print "Your choice: "
sel = gets.chomp.to_f

if sel == 1 then
	while true 
	print "Enter your guess: "
	number =  gets.chomp.to_f
	if number == difficulty['easy'] then
		puts "The number #{number} is right :)"
		tries += 1
		if tries > 1
			puts "You've needed #{tries} tries"
			exit
		else
			puts "You've needed #{tries} try"
		exit
		end
	end
	if number < difficulty['easy'] then
		puts "The number #{number} is too small"
		tries += 1
	end
	if number > difficulty['easy'] then
		puts "The number #{number} is too big"
		tries += 1
	end
	end
end

if sel == 2 then
	while true 
	print "Enter your guess: "
	number =  gets.chomp.to_f
	if number == difficulty['medium'] then
		puts "The number #{number} is right :)"
		tries += 1
		if tries > 1
			puts "You've needed #{tries} tries"
			exit
		else
			puts "You've needed #{tries} try"
		exit
		end
		exit
	end
	if number < difficulty['medium'] then
		puts "The number #{number} is too small"
		tries += 1
	end
	if number > difficulty['medium'] then
		puts "The number #{number} is too big"
		tries += 1
	end
	end
end

if sel == 3 then
	while true 
	print "Enter your guess: "
	number =  gets.chomp.to_f
	if number == difficulty['hard'] then
		puts "The number #{number} is right :)"
		tries += 1
		if tries > 1
			puts "You've needed #{tries} tries"
			exit
		else
			puts "You've needed #{tries} try"
		exit
		end
		exit
	end
	if number < difficulty['hard'] then
		puts "The number #{number} is too small"
		tries += 1
	end
	if number > difficulty['hard'] then
		puts "The number #{number} is too big"
		tries += 1
	end
	end
end

if sel == 4 then
	while true 
	print "Enter your guess: "
	number =  gets.chomp.to_f
	if number == difficulty['very hard'] then
		puts "The number #{number} is right :)"
		tries += 1
		if tries > 1
			puts "You've needed #{tries} tries"
			exit
		else
			puts "You've needed #{tries} try"
		exit
		end
		exit
	end
	if number < difficulty['very hard'] then
		puts "The number #{number} is too small"
		tries += 1
	end
	if number > difficulty['very hard'] then
		puts "The number #{number} is too big"
		tries += 1
	end
	end
end
