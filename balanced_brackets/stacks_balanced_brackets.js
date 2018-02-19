function main() {
    function isBracket(brackets) {
        bracketMatches = {
            '}': '{',
            ')': '(',
            ']': '['
        };
        var checkMatches = [];
        for (var i = 0; i < brackets.length; i++) {
            bracket = brackets.charAt(i);
            if (bracket in bracketMatches) {
                if (bracketMatches[bracket] == checkMatches[checkMatches.length - 1]) {
                    checkMatches.pop();
                } else {
                    return false;
                }
            } else {
                checkMatches.push(bracket);
            }
        }
        if (checkMatches.length == 0) {
            return true;
        } else {
            return false;
        }
    }
    
    var t = parseInt(readLine());
    for(var a0 = 0; a0 < t; a0++){
        var expression = readLine();
        if (isBracket(expression)) {
            console.log("YES");
        } else {
            console.log("NO")
        }
    }
}