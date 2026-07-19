class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int x : nums){
            if(map.containsKey(x)){
                map.put(x,map.get(x)+1);
            }else{
                map.put(x,1);        
            }
        }
        for(int s : map.keySet()){
            if(map.get(s) > nums.length / 2 ){
                return s;
            }
        }
        return -1;
    }
}