text = "The diagram provides information about the life cycle of a star. As we can see, stars originate from the Stellar Nebula and there are 2 alternatives of a star, the Average Star and Massive Star, which each have 4 steps until they reach the end of their life. The Average Star is yellow in color. This first kind of star evolves into the Red Giant, which tends toward reddish-orange. Then, blast and turn into a Planetary Nebula. In the end, condensed into White Dwarf. Meanwhile, the second type of star has the same color as the first form in the prior category of stars. The contrast is noticeably larger than the earlier classification of stars. This huge star will modify to Red Supergiant exhibiting dark red color and explode. The detonation is called Supernova. Finally, this kind of star forms into a Neutron Star or collapse into a Black Hole hole Hole hole."

words = text.lower().split()
duplicates = list()
unique_words = list()

for word in words:
    if any(word in w for w in unique_words):
        if any(word in d for d in duplicates):
            continue
        else:
            duplicates.append(word)
    else:
        unique_words.append(word)

print("Length:", len(words))
print("Duplicates:", duplicates)