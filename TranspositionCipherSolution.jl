

function encrypt_transposition(string::String, key::Int=1)    
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [[], [], [], [], [], [], [], []]
    array_words = []

    # Loop through each column in ciphertext:
    for column in 1:key
        currentIndex = column

        # Keep looping until currentIndex goes past the string length:
        while currentIndex <= length(string)
            # Place the character at currentIndex in string at the
            # end of the current column in the ciphertext list:
            #ciphertext[column] += string[currentIndex]
            append!(ciphertext[column], string[currentIndex])

            # Move currentIndex over:
            currentIndex += key
        end
    
    end

    println(ciphertext)
    println("Transpose:\n", permutedims(ciphertext))
    for array in ciphertext
        push!(array_words, join(array))
    end

    # Convert the ciphertext list into a single string value and return it:
    return join(array_words)
end


text = "Common sense is not so common."
println(encrypt_transposition(text, 8))
