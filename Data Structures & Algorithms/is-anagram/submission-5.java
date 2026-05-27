class Solution {
    public boolean isAnagram(String s, String t) {
        Hashtable<Character, Integer> hash1 = new Hashtable<>();
        //Hashtable<Character, Integer> hash2 = new Hashtable<>();

        for (int i = 0; i < s.length(); i ++) {
            if (hash1.containsKey(s.charAt(i))) {
                hash1.put(s.charAt(i), hash1.get(s.charAt(i)) + 1);
            } else {
                hash1.put(s.charAt(i), 1);
            }
        }

        for (int i = 0; i < t.length(); i ++) {
            char c = t.charAt(i);
            if (hash1.containsKey(c)) {
                if (hash1.get(c) == 1) {
                    hash1.remove(c);
                } else  {
                    hash1.put(c, hash1.get(c) - 1);
                }
            } else {
                return false;
            }
        }

        return hash1.isEmpty();
    }
}
