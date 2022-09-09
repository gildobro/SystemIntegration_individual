import { Router } from "express";
const router = Router();

/**
 * @openapi
 * /docs:
 *    get:
 *     summary: Returns the list of all the ISO dates
 *     description: Get all ISO dates
 *     responses:
 *       200:
 *         description: Returns an array of ISO dates.
 * 
 */
router.get("/dates", (req, res) =>{
    res.send({ dates: []});
});

export default router;