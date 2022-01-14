<h2>Camel Banana Problem</h2>
<p>(Camel Banana problem) A person has 3000 bananas and a camel. The person wants to transport the maximum number of bananas to a destination which is 1000 KMs away, using only the camel as a mode of transportation. The camel cannot carry more than 1000 bananas at a time and eats a banana every km it travels. What is the maximum number of bananas that can be transferred to the destination using only camel (no other mode of transportation is allowed).</p>

<h2>Solution & Procedure</h2>
<p>First of all, the Brute-Force approach does not work. if Camel start by picking up the 1000 bananas and try to reach point B, then Camel will eat up all the 1000 bananas on the way and there will be no banana left for the Camel to return to point A. So we have to take an approach that Camel drop the bananas in between and then return to point A, to pick bananas again. Since there are 3000 bananas and camel can only carry 1000 bananas, Camel will have to make 3 trips to carry them all to any point in between.
  
<p>When bananas are reduced to 2000 then Camel can shift them to another point in 2 trips and when the number of bananas left are</p>

<p>In the first part, P1, to shift the bananas by 1Km Camel will have to:</p>

<ol>
  <li>Move forward with 1000 bananas – Will eat up 1 banana in the way forward.</li>
  <li>Leave 998 banana after 1 km and return with 1 banana – will eat up 1 banana in the way back.</li>
  <li>Pick up the next 1000 bananas and move forward – Will eat up 1 banana in the way forward.</li>
  <li>Will carry the last 1000 bananas from point a and move forward – will eat up 1 banana. Note: After point 5 the camel does not need to return to point A again. So to shift 3000 bananas by 1km Camel will eat up 5 bananas.</li>
  <li>After moving to 200 km the camel would have eaten up 1000 bananas and is now left with 2000 bananas. Hence, the length of part P1 is 200 Km.</li></ol>

<p>Now in the Part P2, the Camel need to do the following to shift the Bananas by 1km:</p>

<ol>
  <li>Move forward with 1000 bananas - Will eat up 1 banana in the way forward.</li>
  <li>Leave 998 banana after 1 km and return with 1 banana - will eat up this 1 banana in the way back.</li>
  <li>Pick up the next 1000 bananas and move forward - Will eat up 1 banana in the way forward. Note: After point 3 the camel does not need to return to the starting point of P2.</li>
  <li>So to shift 2000 bananas by 1km Camel will eat up 3 bananas.</li>
  <li>After moving to 333 km the camel would have eaten up 1000 bananas and is now left with the last 1000 bananas.</li>
  <li>The camel will actually be able to cover 333.33 km. I will ignore the decimal part because it will not make a difference in this example. Hence the length of part P2 is 333 Km.</li></ol>

<p> Now, for the last part, P3, the Camel only has to move forward. He has already covered 533 (200+333) out of 1000 km in Parts P1 & P2. Now he has to cover only 466 km and he has 1000 bananas.</p>

<ul>
  <li>So Finally, He will eat up 466 bananas on the way forward, and at point B the Camel will be left with only 533 Bananas.</li></ul>

