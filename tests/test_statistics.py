from src.statistics import summary

def test_statistics():

    result = summary([
        {
            "favorite": True
        }
    ])

    assert result["favorites"] == 1
