using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LearningCurve : MonoBehaviour
{
	// Start is called before the first frame update
	public int fstnum = 2;
	public int sndnum = 3;
	void Start()
    {
		addnum();
	}

	void addnum()
	{
		Debug.Log(fstnum + sndnum);
	}




}



