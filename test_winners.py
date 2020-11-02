from winners import Winners

# initiate this class for testing
wi = Winners()


def test_constructor():
    # test the class of the "winners" attribute
    # test some initiatial values of attribute variables
    assert type(wi.winners).__name__ == 'dict' and \
           len(wi.winners) == 0 and \
           (wi.answer is None)


def test_winners_update():
    # initiate assumed winner "Jason" and "test_score.txt" for testing
    # before the test, "Jason" had not won before
    filename = "test_score.txt"
    wi.winners_update("Jason", filename)
    # test former info in the test file
    assert wi.winners["test_name_1"] == 56 and \
        wi.winners["test_name_2"] == 46 and \
        wi.winners["test_name_3"] == 36 and \
        wi.winners["test_name_4"] == 26 and \
        wi.winners["test_name_5"] == 16 and \
        wi.winners["test_name_6"] == 6

    # test newly added info in the test file
    assert wi.answer == "Jason" and \
        "Jason" in wi.winners and \
        wi.winners["Jason"] == 1

    # test when "Jason" is added again, if its value will be updated
    wi.winners_update("Jason", filename)
    assert wi.answer == "Jason" and \
        "Jason" in wi.winners and \
        wi.winners["Jason"] == 2


def test_winners_rewrite():
    # before the test, "Jason" had not won before
    filename = "test_score.txt"
    # the third time when "Jason" is called, its value should be 3
    wi.winners_update("Jason", filename)
    assert wi.sorted_count()[0][0] == "test_name_1" and \
        wi.sorted_count()[0][1] == 56 and \
        wi.sorted_count()[1][0] == "test_name_2" and \
        wi.sorted_count()[1][1] == 46 and \
        wi.sorted_count()[2][0] == "test_name_3" and \
        wi.sorted_count()[2][1] == 36 and \
        wi.sorted_count()[3][0] == "test_name_4" and \
        wi.sorted_count()[3][1] == 26 and \
        wi.sorted_count()[4][0] == "test_name_5" and \
        wi.sorted_count()[4][1] == 16 and \
        wi.sorted_count()[5][0] == "test_name_6" and \
        wi.sorted_count()[5][1] == 6

    # the third time when "Jason" is called, its value should be 3
    # still the last one in the returned sorted list
    assert wi.sorted_count()[6][0] == "Jason" and \
        wi.sorted_count()[6][1] == 3


# initiate a dictionary for testing
thisdict = {"item1": 100, "item2": 101, "item3": 2046}


def test_sorted_count():
    # initiate the dictionary for testing
    wi.winners = thisdict
    # make assertions based on the assumed thisdict
    assert wi.sorted_count()[0][0] == "item3" and \
        wi.sorted_count()[0][1] == 2046 and \
        wi.sorted_count()[1][0] == "item2" and \
        wi.sorted_count()[1][1] == 101 and \
        wi.sorted_count()[2][0] == "item1" and \
        wi.sorted_count()[2][1] == 100
