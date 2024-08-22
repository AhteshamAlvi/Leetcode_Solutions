class Solution {
    public boolean isPalindrome(int x) {
        String w = "" + x;
        String pal = "";
        
        for(int i = w.length(); i > 0; i--) {
            pal += w.charAt(i - 1);
        }

        if(pal.equals(w)) {
            return true;
        }
        return false;
    }
}